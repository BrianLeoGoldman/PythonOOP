from abc import ABC, abstractmethod


class Unit(ABC):
    __name = ""
    __life = 0
    __energy = 0
    __stamina = 0

    def __init__(self, name, life, energy, stamina):
        self.__name = name
        self.__life = life
        self.__energy = energy
        self.__stamina = stamina

    def display(self):
        print("Name: " + self.__name +
              " | Life: " + str(self.__life) +
              " | Energy: " + str(self.__energy) +
              " | Stamina: " + str(self.__stamina))

    def weak_attack(self):
        print("This is the weak attack of a unit")

    def strong_attack(self):
        print("This is the strong attack of a unit")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_life(self):
        return self.__life

    def set_life(self, life):
        self.__life = life

    def get_energy(self):
        return self.__energy

    def set_energy(self, energy):
        self.__energy = energy

    def get_stamina(self):
        return self.__stamina

    def set_stamina(self, stamina):
        self.__stamina = stamina


class Warrior(Unit):

    def __init__(self, name, life, energy, stamina):
        super(Warrior, self).__init__(name, life, energy, stamina)

    def weak_attack(self):
        if self.get_stamina() > 3:
            self.set_stamina(self.get_stamina() - 3)
            print("Attacking slowly with an energy of " + str(self.get_energy() / 2))
        else:
            print("Not enough stamina to attack")

    def strong_attack(self):
        if self.get_stamina() > 7:
            self.set_stamina(self.get_stamina() - 7)
            print("Attacking fast with an energy of " + str(self.get_energy()));
        else:
            print("Not enough stamina to attack")


class Wizard:
    __name = ""
    __energy = 0
    __spells = []

    def __init__(self, name, energy):
        self.__name = name
        self.__energy = energy
        self.__spells = []

    def get_name(self):
        return self.__name

    def get_energy(self):
        return self.__energy

    def get_spells(self):
        return self.__spells

    def add_spell(self, spell):
        self.__spells.append(spell)

    def cast_spells(self):
        if self.__energy > len(self.__spells):
            for s in self.__spells:
                s.cast()
            self.__energy = self.__energy - len(self.__spells)
        else:
            print("Not enough energy to cast spells!")

    def dispel_spells(self):
        for s in self.__spells:
            s.dispel()
        self.__spells = []
