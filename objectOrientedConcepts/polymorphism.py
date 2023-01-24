from abc import ABC, abstractmethod


class Executable(ABC):

    @abstractmethod
    def execute(self):
        pass


class Command(Executable):

    def execute(self):
        return "We are implementing the Execute method in Command class"


class Order(Executable):

    def execute(self):
        text = "This is just a text"
        number = 72
        return "We are implementing the Execute method in Order class using text " + text + " and number " + str(number)