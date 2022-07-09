"""
Publisher + subscriber = Observer Pattern
"""
"""
We are designing a weather station ,which outsource the data 
that data is used to power some displays.
Weather station has following data:
    1: Temprature
    2: Pressure
    3: Humidity

Display changes the data whenever the data is updated at published end
"""

from abc import ABCMeta, abstractmethod

class Source(metaclass=ABCMeta):
    @abstractmethod
    def get_temprature(self):
        NotImplementedError

    @abstractmethod
    def get_pressure(self):
        NotImplementedError

    @abstractmethod
    def get_humidity(self):
        NotImplementedError

    @abstractmethod
    def measurement_changed(self):
        NotImplementedError


class Publisher(metaclass=ABCMeta):
    @abstractmethod
    def update_displays(self):
        NotImplementedError


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        NotImplementedError


class WeatherStation(Source):

    @property
    def get_temprature(self):
        return 45

    @property
    def get_pressure(self):
        return .75

    @property
    def get_humidity(self):
        return 94

    def measurement_changed(self, weather_object):
        weather_object.update_displays(self.get_temprature, self.get_pressure, self.get_humidity)


class WeatherObject(Publisher):

    def __init__(self):
        self.displays = []

    def add_display(self, display):
        self.displays.append(display)

    def remove_display(self, display):
        self.displays.remove(display)

    def update_displays(self, temp, press, humid):
        for display in self.displays:
            display.display(temp, press, humid)


class DisplayScreen(Subscriber):
    def display(self, temp, press, humid):
        print(temp, press, humid)


if __name__ == '__main__':
    station = WeatherStation()
    pub = WeatherObject()
    d1 = DisplayScreen()
    d2 = DisplayScreen()
    d3 = DisplayScreen()
    pub.add_display(d1)
    pub.add_display(d2)
    pub.add_display(d3)
    station.measurement_changed(pub)
