from abc import ABC, abstractmethod

class Spell(ABC):

    @abstractmethod
    def cast(self):
        pass

    @abstractmethod
    def dispel(self):
        pass


class IncreaseStamina(Spell):

    __amount = 0
    __is_active = False
    __receiver = ""

    def __init__(self, amount, receiver):
        self.__amount = amount
        self.__is_active = False
        self.__receiver = receiver

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_receiver(self):
        return self.__receiver

    def set_receiver(self, receiver):
        self.__receiver = receiver

    def cast(self):
        self.__receiver.set_stamina(self.__receiver.get_stamina() + self.__amount)
        print("Increased " + self.__receiver.get_name() + " stamina by " + str(self.__amount) + "!")
        self.__is_active = True

    def dispel(self):
        if self.__is_active:
            self.__receiver.set_stamina(self.__receiver.get_stamina() - self.__amount)
            print("Increase stamina spell has been removed from " + self.__receiver.get_name())
        else:
            print("You can't dispel a spell that is not active!")


class RecoverLife(Spell):

    __amount = 0
    __receiver = ""

    def __init__(self, amount, receiver):
        self.__amount = amount
        self.__receiver = receiver

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_receiver(self):
        return self.__receiver

    def set_receiver(self, receiver):
        self.__receiver = receiver

    def cast(self):
        self.__receiver.set_life(self.__receiver.get_life() + self.__amount)
        print(self.__receiver.get_name() + " recovered " + str(self.__amount) + " points of life!")

    def dispel(self):
        # self.__receiver.set_life(self.__receiver.get_life() - self.__amount)
        print("A recover life spell cannot be removed")


class BerserkAttack(Spell):

    __receiver = ""

    def __init__(self, receiver):
        self.__receiver = receiver

    def cast(self):
        self.__receiver.strong_attack()

    def dispel(self):
        print("A berserk attack spell cannot be removed")