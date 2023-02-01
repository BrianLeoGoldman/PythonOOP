from designPatterns.behavioral.observer.observable import WeatherStation
from designPatterns.behavioral.observer.observer import Sprinkler, AirConditioner
from designPatterns.behavioral.strategy.display_behaviour import *
from designPatterns.behavioral.strategy.employee import Employee
from designPatterns.behavioral.strategy.resting_behaviour import *
from designPatterns.behavioral.strategy.working_behaviour import *
from designPatterns.creational.factoryMethod.enemy_factory import RandomEnemyFactory, BalancedEnemyFactory
from designPatterns.structural.decorator.decorators import LaserRobot, NanoRobot, ReactorRobot, BeamRobot
from designPatterns.structural.decorator.robot import SteelRobot, IronRobot
from objectOrientedConcepts.abstraction import Computer
from objectOrientedConcepts.encapsulation import Car
from objectOrientedConcepts.inheritance import Duck, Dog
from objectOrientedConcepts.polymorphism import Command, Order


def encapsulation_test():
    car1 = Car("Toyota", "Corolla", "grey")
    car2 = Car("Ford", "Mondeo", "blue")
    car3 = Car("Chevrolet", "Camaro", "red")
    car1.start()
    car2.start()
    car1.move()
    car1.move()
    car1.stop()
    car3.stop()


def abstraction_test():
    my_computer = Computer()
    my_computer.turn_on()
    my_computer.input_command("image", "photo.jpg")
    my_computer.input_command("text", "story.txt")
    my_computer.input_command("internet", "www.mypage.com")
    my_computer.turn_off()
    # my_computer.processImage("dog.png")
    # AttributeError: 'Computer' object has no attribute 'processImage'
    my_computer._play_game("Undertale")  # Access to a protected member


def inheritance_test():
    animal1 = Duck()
    animal2 = Dog()
    # animal3 = Animal()  TypeError: Can't instantiate abstract class Animal with abstract method eat
    animal1.set_name("Ducky")
    animal1.set_age(2)
    animal2.set_name("Rocky")
    animal2.set_age(5)
    animal1.eat("Grass")
    animal2.eat("Meat")
    animal1.swim()
    animal1.fly()
    animal2.bark()
    animal2.play()
    print("The duck is called " + animal1.get_name() + " and is " + str(animal1.get_age()) + " years old")
    print("The dog is called " + animal2.get_name() + " and is " + str(animal2.get_age()) + " years old")


def polymorphism_test():
    executable1 = Command()
    executable2 = Order()
    executable3 = Command()
    executable4 = Command()
    executable5 = Order()
    executable_list = [executable1, executable2, executable3, executable4, executable5]
    for elem in executable_list:
        print(elem.execute())


def strategy_pattern_test():
    employee = Employee("John", 1, NoWorkingBehaviour(), NoRestingBehaviour(), NoDisplayingBehaviour())

    employee.display()
    employee.rest()
    employee.work()

    employee.set_displaying_behaviour(GraphicDisplayingBehaviour())
    employee.display()
    employee.set_resting_behaviour(HighRestingBehaviour())
    employee.rest()
    employee.set_working_behaviour(TechnicalWorkingBehaviour())
    employee.work()

    employee.set_displaying_behaviour(TextDisplayingBehaviour())
    employee.display()
    employee.set_resting_behaviour(MediumRestingBehaviour())
    employee.rest()
    employee.set_working_behaviour(FinanceWorkingBehaviour())
    employee.work()

    employee.set_resting_behaviour(LowRestingBehaviour())
    employee.rest()
    employee.set_working_behaviour(HRWorkingBehaviour())
    employee.work()


def observer_pattern_test():
    station = WeatherStation()
    sprinkler1 = Sprinkler(station)
    sprinkler2 = Sprinkler(station)
    sprinkler3 = Sprinkler(station)
    air_conditioner1 = AirConditioner(station)
    air_conditioner2 = AirConditioner(station)
    station.register(sprinkler1)
    station.register(sprinkler2)
    station.register(sprinkler3)
    station.register(air_conditioner1)
    station.register(air_conditioner2)
    print("Setting humidity to 46...")
    station.set_humidity(46)
    print("Setting temperature to 26...")
    station.set_temperature(26)
    print("Setting humidity to 34...")
    station.set_humidity(34)
    print("Setting temperature to 29...")
    station.set_temperature(29)
    print("Setting humidity to 31...")
    station.set_humidity(31)
    print("Unregistering one sprinkler and one air conditioner...")
    station.unregister(sprinkler2)
    station.unregister(air_conditioner2)
    print("Setting temperature to 31...")
    station.set_temperature(31)


def decorator_pattern_test():
    steel_robot = SteelRobot()
    decorated_robot1 = LaserRobot(NanoRobot(ReactorRobot(BeamRobot(steel_robot))))
    print(decorated_robot1.get_description())
    print(decorated_robot1.build())

    iron_robot1 = IronRobot()
    decorated_robot2 = LaserRobot(ReactorRobot(ReactorRobot(LaserRobot(iron_robot1))))
    print(decorated_robot2.get_description())
    print(decorated_robot2.build())

    iron_robot2 = IronRobot()
    decorated_robot3 = BeamRobot(iron_robot2)
    print(decorated_robot3.get_description())
    print(decorated_robot3.build())


def factory_method_pattern_test():
    random_factory = RandomEnemyFactory()
    balanced_factory = BalancedEnemyFactory("Soldier")
    random_enemies = []
    balanced_enemies = []
    count = 6
    while count > 0:
        random_enemies.append(random_factory.create_enemy())
        balanced_enemies.append(balanced_factory.create_enemy())
        count = count - 1
    print("Random Enemy Factory")
    for e in random_enemies:
        print(e.display())
    print("Balanced Enemy Factory")
    for e in balanced_enemies:
        print(e.display())


if __name__ == '__main__':
    # Encapsulation
    # encapsulation_test()

    # Abstraction
    # abstraction_test()

    # Inheritance
    # inheritance_test()

    # Polymorphism
    # polymorphism_test()

    # Strategy Pattern
    # strategy_pattern_test()

    # Observer Pattern
    # observer_pattern_test()

    # Decorator Pattern
    # decorator_pattern_test()

    # Factory Method Pattern
    factory_method_pattern_test()
