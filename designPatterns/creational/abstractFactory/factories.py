from abc import ABC, abstractmethod


class CarFactory(ABC):

    @abstractmethod
    def build_chassis(self, code):
        pass

    @abstractmethod
    def build_engine(self, horsepower):
        pass

    @abstractmethod
    def build_radiator(self):
        pass

    @abstractmethod
    def build_battery(self, voltage):
        pass


class FordCarFactory(CarFactory):

    def build_chassis(self, code):
        pass

    def build_engine(self, horsepower):
        pass

    def build_radiator(self):
        pass

    def build_battery(self, voltage):
        pass