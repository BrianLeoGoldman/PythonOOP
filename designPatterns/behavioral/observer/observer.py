from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self):
        pass


class Sprinkler(Observer):

    def __init__(self, station):
        self.__station = station

    def update(self):
        if self.__station.get_humidity() < 35:
            print("Watering the grass because humidity is " + str(self.__station.get_humidity()))


class AirConditioner(Observer):

    def __init__(self, station):
        self.__station = station

    def update(self):
        if self.__station.get_temperature() > 28:
            print("Refreshing the air because temperature is " + str(self.__station.get_temperature()))


