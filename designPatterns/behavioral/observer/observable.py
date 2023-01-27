from abc import ABC, abstractmethod


class Observable(ABC):
    @abstractmethod
    def register(self, observer):
        pass

    @abstractmethod
    def unregister(self, observer):
        pass

    @abstractmethod
    def notify_changes(self):
        pass


class WeatherStation(Observable):

    __humidity = 0
    __temperature = 0
    __observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def unregister(self, observer):
        self.__observers.remove(observer)

    def notify_changes(self):
        for observer in self.__observers:
            observer.update()

    def get_humidity(self):
        return self.__humidity

    def set_humidity(self, humidity):
        self.__humidity = humidity
        self.notify_changes()

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        self.notify_changes()



