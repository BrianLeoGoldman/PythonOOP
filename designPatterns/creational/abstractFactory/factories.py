from abc import ABC, abstractmethod

from designPatterns.creational.abstractFactory.ford import FordChassis, FordEngine, FordRadiator, FordBattery
from designPatterns.creational.abstractFactory.toyota import ToyotaChassis, ToyotaEngine, ToyotaRadiator, ToyotaBattery


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
        return FordChassis(code)

    def build_engine(self, horsepower):
        return FordEngine(horsepower)

    def build_radiator(self):
        return FordRadiator()

    def build_battery(self, voltage):
        if voltage > 10:
            return FordBattery()
        else:
            raise Exception("Not enough voltage to build a Ford battery")


class ToyotaCarFactory(CarFactory):

    def build_chassis(self, code):
        return ToyotaChassis(code)

    def build_engine(self, horsepower):
        return ToyotaEngine(horsepower)

    def build_radiator(self):
        return ToyotaRadiator()

    def build_battery(self, voltage):
        if voltage > 12:
            return ToyotaBattery()
        else:
            raise Exception("Not enough voltage to build a Toyota battery")