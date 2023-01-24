from objectOrientedConcepts.abstraction import Computer
from objectOrientedConcepts.encapsulation import Car
from objectOrientedConcepts.inheritance import Duck, Dog
from objectOrientedConcepts.polymorphism import Command, Order

if __name__ == '__main__':
    # Encapsulation
    car1 = Car("Toyota", "Corolla", "grey")
    car2 = Car("Ford", "Mondeo", "blue")
    car3 = Car("Chevrolet", "Camaro", "red")
    car1.start()
    car2.start()
    car1.move()
    car1.move()
    car1.stop()
    car3.stop()

    # Abstraction
    myComputer = Computer()
    myComputer.turn_on()
    myComputer.input_command("image", "photo.jpg")
    myComputer.input_command("text", "story.txt")
    myComputer.input_command("internet", "www.mypage.com")
    myComputer.turn_off()
    # myComputer.processImage("dog.png")
    # AttributeError: 'Computer' object has no attribute 'processImage'
    myComputer._play_game("Undertale")  # Access to a protected member

    # Inheritance
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

    # Polymorphism
    executable1 = Command()
    executable2 = Order()
    executable3 = Command()
    executable4 = Command()
    executable5 = Order()
    executableList = [executable1, executable2, executable3, executable4, executable5]
    for elem in executableList:
        print(elem.execute())
