from abc import ABC, abstractmethod


class Robot(ABC):

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class IronRobot(Robot):

    def build(self):
        return "[|---|]"

    def get_description(self):
        return "Robot made of iron that builds stuff"


class SteelRobot(Robot):

    def build(self):
        return "[-|||-]"

    def get_description(self):
        return "Robot made of steel that builds stuff"
