import logging
import socket
import uuid
from pykafka.Config import Config
from pykafka.Customer import customer_to_dict
from pykafka.CustomerSchema import CustomerSchema
from pykafka.DataStream import DataStream
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka import Producer


class KafkaProducer:
    """
    This class uses the supplied configuration and a data stream to write to kafka.
    see <https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/avro_producer.py>
    """

    def __init__(self, config: Config, datastream: DataStream):
        self.config = config
        self.datastream = datastream
        self.errors = 0
        self.success = 0

        customer_schema = CustomerSchema()
        key_schema, value_schema = customer_schema.schema()

        schema_registry_client = SchemaRegistryClient({
            'url': config.schema_registry
        })

        self.avro_serializer = AvroSerializer(
            schema_registry_client,
            value_schema,
            customer_to_dict
        )

        self.producer = Producer({
            'bootstrap.servers': config.bootstrap,
            'client.id': socket.gethostname()
        })

    def execute(self):
        """
        When called, will use the configuration and data stream to write to Kafka
        """
        logging.info('Started')

        for _ in range(self.config.count):
            customer = next(self.datastream.data_stream())
            key = str(uuid.uuid4())
            self.producer.produce(
                topic=self.config.topic,
                key=key,
                value=self.avro_serializer(customer, SerializationContext(self.config.topic, MessageField.VALUE)),
                on_delivery=self.send_report
            )

        # Block until the messages are sent.
        remaining = self.producer.poll(10)
        if remaining > 0:
            logging.warning(f'{remaining} messages were still in the queue waiting to go')
        self.producer.flush()
        self.datastream.data_stream().close()

        logging.info(f'Stopped - {self.errors} errors, {self.success} sent')

    def send_report(self, err, _):
        if err is not None:
            self.errors += 1
            logging.error(f'Failed to send message: {str(err)}')
        else:
            self.success += 1
