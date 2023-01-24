from designPatterns.behavioral.strategy.working_behaviour import *
from designPatterns.behavioral.strategy.resting_behaviour import *


class Employee:

    __name: ""
    __code: 0
    __working_behaviour: NoWorkingBehaviour()
    __resting_behaviour: NoRestingBehaviour()
    __displaying_behaviour: NoDisplayingBehaviour()

    # CONSTRUCTOR (for constructor dependency injection)

    def __init__(self, name, code, working_behaviour, resting_behaviour, display_behaviour):
        self.__name = name
        self.__code = code
        self.__working_behaviour = working_behaviour
        self.__resting_behaviour = resting_behaviour
        self.__displaying_behaviour = display_behaviour

    # SETTERS (for setter dependency injection)

    def set_working_behaviour(self, working_behaviour):
        self.__working_behaviour = working_behaviour

    def set_resting_behaviour(self, resting_behaviour):
        self.__resting_behaviour = resting_behaviour

    def set_displaying_behaviour(self, displaying_behaviour):
        self.__displaying_behaviour = displaying_behaviour

    # METHODS

    def work(self):
        self.__working_behaviour.work()

    def rest(self):
        self.__resting_behaviour.rest()

    def display(self):
        self.__resting_behaviour.rest()