from abc import ABC, abstractmethod


class Animal(ABC):  # Abstract class (or interface)
    __name = ""
    __age = ""

    def getName(self):  # Getter for name
        return self.__name

    def getAge(self):  # Getter for age
        return self.__age

    def setName(self, name):  # Setter for name
        self.__name = name

    def setAge(self, age):  # Setter for age
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

