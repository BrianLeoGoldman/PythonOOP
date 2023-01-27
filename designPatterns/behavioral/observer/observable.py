from abc import ABC, abstractmethod


class Observable(ABC):
    @abstractmethod
    def register(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notifyChanges(self):
        pass


class WeatherStation(Observable):

    __humidity = 0
    __temperature = 0
    __observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def remove(self, observer):
        self.__observers.remove(observer)

    def notifyChanges(self):
        for observer in self.__observers:
            observer.update()
