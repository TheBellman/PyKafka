from pykafka.DataStream import DataStream
from faker import Faker


class StringDataStream(DataStream):
    """
    implementation of DataStream that returns the data as strings
    """

    def __init__(self):
        self.fake = Faker()

    def data_list(self, count):
        return [next(self.data_stream()) for _ in range(count)]

    def data_stream(self):
        while True:
            yield self.fake.name()
