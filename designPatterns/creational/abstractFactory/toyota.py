from designPatterns.creational.abstractFactory.truck import Chassis, Engine, Battery, Radiator


class ToyotaChassis(Chassis):

    def __init__(self, code):
        super(ToyotaChassis, self).__init__(code)


class ToyotaEngine(Engine):

    def __init__(self, horsepower):
        super(ToyotaEngine, self).__init__(horsepower)


class ToyotaBattery(Battery):

    def turn_on(self):
        return "Turning on the Toyota battery"

    def turn_off(self):
        return "Turning off the Toyota battery"


class ToyotaRadiator(Radiator):

    def cool_engine(self):
        return "Cooling engine with the Toyota radiator"

    def heat_cabin(self):
        return "Heating the cabin with the Toyota radiator"
