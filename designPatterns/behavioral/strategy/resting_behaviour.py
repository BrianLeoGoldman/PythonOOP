from abc import ABC, abstractmethod


class RestingBehaviour(ABC):  # Abstract class (or interface)

    @abstractmethod
    def rest(self):
        pass


class NoRestingBehaviour(RestingBehaviour):

    def rest(self):
        print("No resting for me...")


class LowRestingBehaviour(RestingBehaviour):

    def rest(self):
        time_to_rest = 1
        print("Resting for " + str(time_to_rest) + " hours...")


class MediumRestingBehaviour(RestingBehaviour):

    def rest(self):
        player1 = "Samuel"
        player2 = "Johanna"
        print("Playing a poker match with " + player1 + " and " + player2)


class HighRestingBehaviour(RestingBehaviour):

    def rest(self):
        destination = "San Francisco, California"
        days = 10
        money = 10000
        while days > 0:
            print("Resting in " + destination + " with " + money + " dollars")
            days = days - 1
            money = money - 750
