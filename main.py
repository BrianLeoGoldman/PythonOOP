from abstraction import Computer
from encapsulation import Car
from inheritance import Duck, Dog, Animal
from polymorphism import Command, Order

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
    myComputer.turnOn()
    myComputer.inputCommand("image", "photo.jpg")
    myComputer.inputCommand("text", "story.txt")
    myComputer.inputCommand("internet", "www.mypage.com")
    myComputer.turnOff()
    # myComputer.processImage("dog.png")
    # AttributeError: 'Computer' object has no attribute 'processImage'
    myComputer._playGame("Undertale")  # Access to a protected member

    # Inheritance
    animal1 = Duck()
    animal2 = Dog()
    # animal3 = Animal()  TypeError: Can't instantiate abstract class Animal with abstract method eat
    animal1.setName("Ducky")
    animal1.setAge(2)
    animal2.setName("Rocky")
    animal2.setAge(5)
    animal1.eat("Grass")
    animal2.eat("Meat")
    animal1.swim()
    animal1.fly()
    animal2.bark()
    animal2.play()
    print("The duck is called " + animal1.getName() + " and is " + str(animal1.getAge()) + " years old")
    print("The dog is called " + animal2.getName() + " and is " + str(animal2.getAge()) + " years old")

    # Polymorphism
    executable1 = Command()
    executable2 = Order()
    executable3 = Command()
    executable4 = Command()
    executable5 = Order()
    executableList = [executable1, executable2, executable3, executable4, executable5]
    for elem in executableList:
        print(elem.execute())
