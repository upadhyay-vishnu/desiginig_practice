"""
This implementation is slightly different
Optimzations
1: Weather Station can have any number of data points, 
2: Weather publishers is bound to weather station, but station can have multiple weather publishers
3: Display can have only 1 publisher also
"""



from abc import ABCMeta, abstractmethod


class DataPoints(metaclass=ABCMeta):
    @abstractmethod
    def data_value(self):
        NotImplementedError

    @abstractmethod
    def data_unit(self):
        NotImplementedError

    @abstractmethod
    def data_output(self):
        NotImplementedError


class TempratureDataPoint(DataPoints):
    def data_value(self):
        return 42

    def data_unit(self):
        return 'selcius'

    def data_output(self):
        return self.data_value() + ' ' + self.data_unit()


class SourceDataPoints:
    def add_data_point(self):
        pass


class Source(metaclass=ABCMeta):
    pass
