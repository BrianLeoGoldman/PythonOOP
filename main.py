from designPatterns.behavioral.strategy.display_behaviour import *
from designPatterns.behavioral.strategy.employee import Employee
from designPatterns.behavioral.strategy.resting_behaviour import *
from designPatterns.behavioral.strategy.working_behaviour import *
from objectOrientedConcepts.abstraction import Computer
from objectOrientedConcepts.encapsulation import Car
from objectOrientedConcepts.inheritance import Duck, Dog
from objectOrientedConcepts.polymorphism import Command, Order


def encapsulationTest():
    car1 = Car("Toyota", "Corolla", "grey")
    car2 = Car("Ford", "Mondeo", "blue")
    car3 = Car("Chevrolet", "Camaro", "red")
    car1.start()
    car2.start()
    car1.move()
    car1.move()
    car1.stop()
    car3.stop()


def abstractionTest():
    my_computer = Computer()
    my_computer.turn_on()
    my_computer.input_command("image", "photo.jpg")
    my_computer.input_command("text", "story.txt")
    my_computer.input_command("internet", "www.mypage.com")
    my_computer.turn_off()
    # my_computer.processImage("dog.png")
    # AttributeError: 'Computer' object has no attribute 'processImage'
    my_computer._play_game("Undertale")  # Access to a protected member


def inheritanceTest():
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


def polymorphismTest():
    executable1 = Command()
    executable2 = Order()
    executable3 = Command()
    executable4 = Command()
    executable5 = Order()
    executable_list = [executable1, executable2, executable3, executable4, executable5]
    for elem in executable_list:
        print(elem.execute())


def strategyPatternTest():
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


if __name__ == '__main__':
    # Encapsulation
    # encapsulationTest()

    # Abstraction
    # abstractionTest()

    # Inheritance
    # inheritanceTest()

    # Polymorphism
    # polymorphismTest()

    # Strategy Pattern
    strategyPatternTest()
