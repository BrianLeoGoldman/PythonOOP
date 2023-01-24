from abc import ABC, abstractmethod


class Animal(ABC):  # Abstract class (or interface)
    __name = ""
    __age = ""

    def get_name(self):  # Getter for name
        return self.__name

    def get_age(self):  # Getter for age
        return self.__age

    def set_name(self, name):  # Setter for name
        self.__name = name

    def set_age(self, age):  # Setter for age
        self.__age = age

    @abstractmethod
    def eat(self, food):
        # print("Eating the food " + food)
        pass


class Dog(Animal):

    def bark(self):
        print("Barking to the cats...")

    def play(self):
        print("Playing with a human...")

    def eat(self, food):
        print("Eating the food " + food + " as a dog")


class Duck(Animal):

    def swim(self):
        print("Swimming in the water...")

    def fly(self):
        print("Flying through the sky...")

    def eat(self, food):
        print("Eating the food " + food + " as a duck")

