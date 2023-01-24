from abc import ABC, abstractmethod


class DisplayingBehaviour(ABC):  # Abstract class (or interface)

    @abstractmethod
    def display(self, name, code):
        pass


class NoDisplayingBehaviour(DisplayingBehaviour):

    def display(self, name, code):
        print("I have nothing to show you...")


class TextDisplayingBehaviour(DisplayingBehaviour):

    def display(self, name, code):
        print("Employee name is " + name + " and employee code is " + str(code))


class GraphicDisplayingBehaviour(DisplayingBehaviour):

    def display(self, name, code):
        image = "///-\\\\\\\n" + "|^   ^|\n" + "|O   O|\n" + "|  ~  |\n" + " \\ O /\n" + "  | |"
        print(image + "\n" + name + " - " + code)
