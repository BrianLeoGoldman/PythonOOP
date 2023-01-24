class Computer:

    def turnOn(self):
        print("Turning on the computer")

    def inputCommand(self, command, value):
        if command == "image":
            self.__processImage(value)
        elif command == "text":
            self.__processText(value)
        elif command == "internet":
            self.__connectToTheWeb(value)
        else:
            print("Nothing to do...")

    def turnOff(self):
        print("Turning off the computer")

    def __processImage(self, image):  # Private method
        print("Processing image " + image)

    def __processText(self, text):  # Private method
        print("Processing text " + text)

    def __connectToTheWeb(self, webPage):  # Private method
        print("Connecting to " + webPage)

    def _playGame(self, game):
        print("Playing " + game)
