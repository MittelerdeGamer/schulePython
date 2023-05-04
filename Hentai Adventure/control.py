import random
from enemies import Enemy
from hero import Hero


class Control:
    __hero: Hero

    def main(self):
        print("Start a new Game. Create Character.")
        name = input("Please choose a name: ")
        print("Character created")
        self.__hero = Hero(name)

        end = False
        while not end:
            print("*** Stats(Day " + str(self.__hero.getDays()) + ") ***")
            print("Name: " + self.__hero.getName())
            print("Stamina: " + str(self.__hero.getStamina()))
            print("Gold: " + str(self.__hero.getGold()))
            print("Level: " + str(self.__hero.getLevel()))

            print("Choose an action?")
            print("1 - rest")
            print("2 - train")
            print("3 - shop")
            print("4 - go to forest")
            print("0 - end game")
            selectedAction = input("Please choose: ")

            if selectedAction == "1":
                self.__hero.rest()
            elif selectedAction == "2":
                self.__hero.train()
            elif selectedAction == "3":
                pass
            elif selectedAction == "4":
                self.goToForest()
            elif selectedAction == "0":
                end = True
            else:
                print("Invalid input")

    def goToForest(self):
        enemyCount = random.randint(1, 3)
        enemyList = []
        for i in range(enemyCount):
            e = Enemy(self.__hero.getLevel())
            enemyList.append(e)
        print(str(enemyCount) + " enemies appeared")
        print("1 - fight")
        print("2 - run")
        selectedAction = input("Please choose: ")
        if selectedAction == "1":
            for f in enemyList:
                if self.simulateFight():
                    #Win
                    print(self.__hero.getName() + " won the fight.")
                    self.__hero.lootGold(f.getLootGold())
                else:
                    #Lose
                    print(self.__hero.getName() + " lost the fight.")
                    self.__hero.fightLost()
        else:
            print(self.__hero.getName() + " ran away.")

    def simulateFight(self):
        r = random.randint(1, 1000)
        result = r % 100
        return result < self.__hero.getWinBonus()
