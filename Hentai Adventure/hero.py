class Hero:
    __name: str
    __gold: int
    __itemList: list
    __stamina: int
    __level: int
    __days: int
    __winBonus: int

    def __init__(self, name):
        self.__name = name
        self.__gold = 0
        self.__itemList = []
        self.__stamina = 20
        self.__level = 1
        self.__days = 0
        self.__winBonus = 50

    def rest(self):
        self.__stamina = self.__level * 20
        self.__days = self.__days + 1

    def train(self):
        if self.__gold < 1000:
            print(self.getName() + " does not have enough gold to train.")
            return
        self.__gold = self.__gold - 1000
        self.__level = self.__level + 1

    def fightLost(self):
        if self.__stamina - (self.__stamina / 2) <= 0:
            self.die()
        else:
            self.__stamina = int(self.__stamina / 2)

    def die(self):
        print(self.getName() + " got hurt badly and has to rest for a bit.")
        self.__gold = int(self.__gold / 2)
        self.rest()

    def lootGold(self, lootGold: int):
        self.__gold = self.__gold + lootGold

    # Getter und Setter

    def getStamina(self):
        return self.__stamina

    def getName(self):
        return self.__name

    def getLevel(self):
        return self.__level

    def getDays(self):
        return self.__days

    def getWinBonus(self):
        return self.__winBonus

    def getGold(self):
        return self.__gold
