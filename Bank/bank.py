import random


class Account:
    __kontostand: int

    def __init__(self, kontostand: int):
        self.__kontostand = kontostand

    def get_kontostand(self) -> int:
        return self.__kontostand


class Bank:
    __kontenliste: list

    def __init__(self):
        self.__kontenliste = []

    def add_account(self, kontostand: int):
        self.__kontenliste.append(Account(kontostand))

    def calculate_summ(self) -> int:
        summ = 0
        for konto in self.__kontenliste:
            summ = summ + konto.get_kontostand()
        return summ


def main():
    bank1 = Bank()
    for i in range(random.randint(10, 250)):
        bank1.add_account(random.randint(0, 10000))
    print(bank1.calculate_summ())


if __name__ == "__main__":
    main()
