class Computer:

    def turn_on(self):
        print("Turning on the computer")

    def input_command(self, command, value):
        if command == "image":
            self.__process_image(value)
        elif command == "text":
            self.__process_text(value)
        elif command == "internet":
            self.__connect_to_the_web(value)
        else:
            print("Nothing to do...")

    def turn_off(self):
        print("Turning off the computer")

    def __process_image(self, image):  # Private method
        print("Processing image " + image)

    def __process_text(self, text):  # Private method
        print("Processing text " + text)

    def __connect_to_the_web(self, web_page):  # Private method
        print("Connecting to " + web_page)

    def _play_game(self, game):
        print("Playing " + game)
