

class Manager:

    __instance = None
    __code = 0

    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(self):
        if self.__instance is None:
            print('Creating new instance')
            self.__instance = self.__new__(self)
            # Initialization goes here
        return self.__instance

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code