from abc import ABC, abstractmethod


class Enemy(ABC):
    __life = 0
    __strength = 0
    __reward = ""

    def __init__(self, life, strength, reward):
        self.__life = life
        self.__strength = strength
        self.__reward = reward

    def attack(self):
        return self.__strength

    def receive_attack(self, impact):
        self.__life = self.__life - impact

    def display(self):
        return "Life: " + str(self.__life) + " | Strength: " + str(
            self.__strength) + " | Reward: " + self.__reward + "]"


class Soldier(Enemy):

    def __init__(self, life, strength, reward):
        super().__init__(life, strength, reward)

    def attack(self):
        return super().attack() + 10

    def display(self):
        return "[Soldier => " + super().display()


class Monster(Enemy):

    def __init__(self, life, strength, reward):
        super().__init__(life, strength, reward)

    def attack(self):
        return super().attack() * 2

    def display(self):
        return "[Monster => " + super().display()


class Ghost(Enemy):

    def __init__(self, life, strength, reward):
        super().__init__(life, strength, reward)

    def attack(self):
        return super().attack() - 3

    def receive_attack(self, impact):
        self.__life = self.__life - impact + 5

    def display(self):
        return "[Ghost => " + super().display()