from abc import ABC, abstractmethod


class DataStream(ABC):
    """
    base class to represent a data source
    """

    @abstractmethod
    def data_list(self, count):
        """
        return the data as a simple list containing count items
        :param count: the number of items to build
        :return: the list containing count items
        """
        pass

    @abstractmethod
    def data_stream(self):
        """
        return the data via a generator
        :return: a generator that produces data
        """
        pass