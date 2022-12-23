from pykafka.DataStream import DataStream
from faker import Faker


class StringDataStream(DataStream):
    """
    implementation of DataStream that returns the data as strings
    """

    def __init__(self):
        self.fake = Faker()

    def data_list(self, count):
        return [self.fake.name() for _ in range(count)]
