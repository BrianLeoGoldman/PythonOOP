class Car:
    # Class attributes/properties
    # brand = ""
    # model = ""
    # color = ""

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def start(self):
        print("Starting engine...")

    def stop(self):
        print("Stopping engine...")

    def move(self):
        print("Moving car with brand " + self.brand + " and model " + self.model + " and color " + self.color)


