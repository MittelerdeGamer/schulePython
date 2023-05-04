import random


class Enemy:
    __stamina: int
    __lootGold: int

    def __init__(self, charlevel: int):
        self.__stamina = random.randint(0, charlevel * 20)
        self.__lootGold = random.randint(0, charlevel * 15)

    def getLootGold(self):
        return self.__lootGold

