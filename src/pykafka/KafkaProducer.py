import logging
import socket
import uuid
from pykafka.Config import Config
from pykafka.DataStream import DataStream
from confluent_kafka import Producer


class KafkaProducer:
    """
    This class uses the supplied configuration and a data stream to write to kafka.
    """

    def __init__(self, config: Config, datastream: DataStream):
        self.config = config
        self.datastream = datastream
        self.producer = Producer(
            {
                'bootstrap.servers': config.bootstrap,
                'client.id': socket.gethostname()
            }
        )

    def execute(self):
        """
        When called, will use the configuration and data stream to write to Kafka
        """
        logging.info('Started')

        for _ in range(self.config.count):
            name = next(self.datastream.data_stream())
            self.producer.produce(self.config.topic, key=str(uuid.uuid4()), value=name, callback=self.error_logger)
            logging.info(f'name = {name}')

        self.producer.flush()
        self.datastream.data_stream().close()
        logging.info('Stopped')

    @staticmethod
    def error_logger(err, _):
        if err is not None:
            logging.error(f'Failed to send message: {str(err)}')

