import random
from tools import fakultaetBAD


def aufg2():
    anzahl = 6
    i = 0
    summe = 0
    temperaturen = []  # Anlegen einer leeren Liste
    while i < anzahl:
        print("Geben Sie die {0}. Temperatur in ° C ein".format(i + 1))
        eingabe = float(input())
        temperaturen.append(eingabe)  # Element am Ende der Liste hinzufügen
        summe = summe + eingabe  # Summe von allen Werten
        i = i + 1
    durchschnitt = summe / anzahl

    print("Durchschnitt: " + str(durchschnitt) + "°C")

    for j in range(0, anzahl):
        print(str(temperaturen[j]) + "°C am Tag " + str(j + 1))


def aufg3():
    anzahl = 31
    i = 0
    summe = 0
    temperaturen = []  # Anlegen einer leeren Liste
    rand = random
    rand.seed()

    while i < anzahl:
        eingabe = float(rand.randint(0, 25))
        temperaturen.append(eingabe)  # Element am Ende der Liste hinzufügen
        summe = summe + temperaturen[i]  # auf Listenelement zugreifen
        i = i + 1
    durchschnitt = summe / anzahl

    print("Durchschnitt: " + str(durchschnitt) + "°C")

    for j in range(0, anzahl):
        print(str(temperaturen[j]) + "°C am Tag " + str(j + 1))


def aufg4():
    for i in range(0, 21):
        if i % 2 == 0:
            print(i)


def aufg5():
    anzahl = 20

    odd = 0
    if anzahl % 2 == 0:
        odd = anzahl + 1
    else:
        odd = anzahl

    for i in range(anzahl, 0, -1):

        if i % 2 == 0:
            print()
        else:
            s = "\t"
            offset = int((odd - i) / 2)
            for j in range(0, offset):
                s = s + " "
            for j in range(0, i):
                s = s + "*"
            for j in range(0, offset):
                s = s + " "
            print(s + "\t" + str(i) + " Sterne")


def aufg6():
    n = int(input("Geben sie die Fakultät ein: "))
    print("Fakultät von " + str(n) + " bertägt: " + str(fakultaetBAD(n)))
