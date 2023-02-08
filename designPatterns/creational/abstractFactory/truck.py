from abc import ABC, abstractmethod


class Truck:
    __chassis = ""
    __engine = ""
    __radiator = ""
    __battery = ""

    def get_chassis(self):
        return self.__chassis

    def set_chassis(self, chassis):
        self.__chassis = chassis

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine):
        self.__engine = engine

    def get_radiator(self):
        return self.__radiator

    def set_radiator(self, radiator):
        self.__radiator = radiator

    def get_battery(self):
        return self.__battery

    def set_battery(self, battery):
        self.__battery = battery


class Chassis(ABC):
    __code = 0

    def __init__(self, code):
        self.__code = code

    def get_code(self):
        return self.__code


class Engine(ABC):
    __horsepower = 0

    def __init__(self, horsepower):
        self.__horsepower = horsepower

    def get_horsepower(self):
        return self.__horsepower

    def start(self):
        return "Starting engine of " + str(self.__horsepower) + " HP"

    def stop(self):
        return "Stopping engine of " + str(self.__horsepower) + " HP"


class Battery(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Radiator(ABC):

    @abstractmethod
    def cool_engine(self):
        pass

    @abstractmethod
    def heat_cabin(self):
        pass
