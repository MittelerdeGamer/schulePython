class Counter:

    def __init__(self):
        self.__counter = 0

    def count(self):
        self.__counter = self.__counter + 1

    def reset(self):
        self.__counter = 0

    def getCount(self):
        return self.__counter
