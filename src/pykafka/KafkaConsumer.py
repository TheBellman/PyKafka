import logging

from confluent_kafka.cimpl import Consumer, KafkaError, KafkaException
from confluent_kafka.schema_registry import SchemaRegistryClient
from pykafka.Config import Config
from pykafka.Customer import customer_from_dict
from pykafka.CustomerSchema import CustomerSchema
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import SerializationContext, MessageField

MIN_COMMIT_COUNT = 10


class KafkaConsumer:
    """
    This class uses the supplied configuration and a data stream to write to kafka.
    """

    def __init__(self, config: Config):
        self.config = config
        self.errors = 0
        self.success = 0
        self.running = True

        customer_schema = CustomerSchema()
        key_schema, value_schema = customer_schema.schema()

        schema_registry_client = SchemaRegistryClient({
            'url': config.schema_registry
        })

        self.avro_deserializer = AvroDeserializer(schema_registry_client,
                                                  value_schema,
                                                  customer_from_dict)

        self.consumer = Consumer(
            {
                'bootstrap.servers': config.bootstrap,
                'group.id': 'pykafka',
                'auto.offset.reset': 'earliest',
                'on_commit': self.commit_completed
            }
        )

    def execute(self):
        """
        when called, will start a poll loop that just pulls the messages and logs them.

        see <https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/avro_consumer.py>
        """
        logging.info('Started')
        self.consumer.subscribe([self.config.topic])
        msg_count = 0

        try:
            while self.running:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    logging.info('waiting...')
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        logging.error(f'{msg.topic()} {msg.partition()} reached end at offset {msg.offset()}')
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    customer = self.avro_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))
                    if customer is not None:
                        logging.info(f'{msg.key()} : {customer}')
                    msg_count += 1
                    if msg_count % MIN_COMMIT_COUNT == 0:
                        self.consumer.commit(asynchronous=True)

        except KeyboardInterrupt:
            self.shutdown()
        finally:
            self.consumer.close()

        logging.info(f'Stopped - comsumed {msg_count} messages')

    def shutdown(self):
        self.running = False

    @staticmethod
    def commit_completed(err, partitions):
        if err:
            logging.error(str(err))
        else:
            logging.info(f'Committed partition offsets: {str(partitions)}')
