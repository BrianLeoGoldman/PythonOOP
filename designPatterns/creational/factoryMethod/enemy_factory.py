from abc import ABC, abstractmethod
import random

from designPatterns.creational.factoryMethod.enemy import Soldier, Monster, Ghost


class EnemyFactory(ABC):

    @abstractmethod
    def create_enemy(self):
        pass


class RandomEnemyFactory(EnemyFactory):

    def create_enemy(self):
        enemy_type = random.randint(0, 3)
        if enemy_type == 0:
            life = random.randint(40, 120)
            strength = random.randint(30, 80)
            return Soldier(life, strength, "Potion")
        if enemy_type == 1:
            life = random.randint(70, 250)
            strength = random.randint(120, 260)
            return Monster(life, strength, "Claw")
        else:
            life = random.randint(70, 170)
            strength = random.randint(60, 80)
            return Ghost(life, strength, "Ectoplasm")


class BalancedEnemyFactory(EnemyFactory):
    __last_enemy_created = ""

    def __init__(self, first_enemy_to_create):
        self.__last_enemy_created = first_enemy_to_create

    def create_enemy(self):
        if self.__last_enemy_created == "Soldier":
            self.__last_enemy_created = "Monster"
            return Monster(200, 100, "Claw")
        if self.__last_enemy_created == "Monster":
            self.__last_enemy_created = "Ghost"
            return Ghost(90, 90, "Ectoplasm")
        else:
            self.__last_enemy_created = "Soldier"
            return Soldier(120, 110, "Potion")
