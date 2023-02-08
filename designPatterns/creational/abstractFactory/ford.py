from designPatterns.creational.abstractFactory.truck import Chassis, Engine, Battery, Radiator


class FordChassis(Chassis):

    def __init__(self, code):
        super(FordChassis, self).__init__(code)


class FordEngine(Engine):

    def __init__(self, horsepower):
        super(FordEngine, self).__init__(horsepower)


class FordBattery(Battery):

    def turn_on(self):
        return "Turning on the Ford battery"

    def turn_off(self):
        return "Turning off the Ford battery"


class FordRadiator(Radiator):

    def cool_engine(self):
        return "Cooling engine with the Ford radiator"

    def heat_cabin(self):
        return "Heating the cabin with the Ford radiator"
