import random
from abc import ABC, abstractmethod


class WorkingBehaviour(ABC):  # Abstract class (or interface)

    @abstractmethod
    def work(self):
        pass


class TechnicalWorkingBehaviour(WorkingBehaviour):

    def work(self):
        languages = ["Java", "Python", "Ruby"]
        random_element = random.choice(languages)
        print("Coding with " + random_element)


class FinanceWorkingBehaviour(WorkingBehaviour):

    def work(self):
        money1 = 30800
        money2 = 60900
        money3 = 21000
        money4 = 77980
        print("Transferring " + str(money1 + money2 + money3 + money4) + " to a new account")


class HRWorkingBehaviour(WorkingBehaviour):

    def work(self):
        employee1 = "Gabriella"
        employee2 = "Tomas"
        employee3 = "Mark"
        print("Resolving issues between " + employee1 + " and " + employee2 + " and firing " + employee3)
