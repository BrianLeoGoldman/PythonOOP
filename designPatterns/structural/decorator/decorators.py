from abc import ABC, abstractmethod

from designPatterns.structural.decorator.robot import Robot


class RobotDecorator(Robot):
    __robot = ""

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class BeamRobot(RobotDecorator):

    def __init__(self, robot):
        self.__robot = robot

    def build(self):
        return self.__robot.build() + "-(0)-"

    def get_description(self):
        return self.__robot.get_description() + " equipped with beams"


class LaserRobot(RobotDecorator):

    def __init__(self, robot):
        self.__robot = robot

    def build(self):
        return self.__robot.build() + "*---*"

    def get_description(self):
        return self.__robot.get_description() + " equipped with lasers"


class NanoRobot(RobotDecorator):

    def __init__(self, robot):
        self.__robot = robot

    def build(self):
        return self.__robot.build() + "-0-0-0-0-"

    def get_description(self):
        return self.__robot.get_description() + " equipped with nanotechnology"


class ReactorRobot(RobotDecorator):

    def __init__(self, robot):
        self.__robot = robot

    def build(self):
        return self.__robot.build() + "===|==="

    def get_description(self):
        return self.__robot.get_description() + " equipped with a reactor"
