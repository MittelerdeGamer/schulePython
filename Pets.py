class Pet:

    def __init__(self, name):
        self.__name = name

    def eat(self):
        print(f"{self.getName()}: *eating sounds*")

    def getName(self):
        return self.__name


class Cat(Pet):

    def __init__(self, name):
        super().__init__(name)
        self.__countLives = 9

    def makeCatNoice(self):
        print(f"{self.getName()}: meow")


class Dog(Pet):

    def __init__(self, name):
        super().__init__(name)
        self.__family = 0
        self.__brave = 0

    def bark(self):
        print(f"{self.getName()}: Wuff")
        self.__brave = self.__brave - 2
        self.__family = self.__family - 1

    def bite(self):
        if self.__brave <= 0:
            if self.__family <= 0:
                print(f"{self.getName()}: *bites*")
        else:
            print(f"{self.getName()}: *does not bite*")

    def petting(self, minutes):
        self.__brave = self.__brave + minutes
        self.__family = self.__family + minutes

    def treat(self, count):
        self.__brave = self.__brave + (5*count)
        self.__family = self.__family + (2*count)

