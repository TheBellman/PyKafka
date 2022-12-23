import logging
from pykafka.Config import Config
from pykafka.DataStream import DataStream


class Producer:
    """
    This class uses the supplied configuration and a data stream to write to kafka.
    """
    def __init__(self, config: Config, datastream: DataStream):
        self.config = config
        self.datastream = datastream

    """
    When called, will use the configuration and data stream to write to Kafka
    """
    def execute(self):
        logging.info('Started')

        for _ in range(self.config.count):
            name = next(self.datastream.data_stream())
            logging.info(f'name = {name}')

        self.datastream.data_stream().close()
        logging.info('Stopped')
