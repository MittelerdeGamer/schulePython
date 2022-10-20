import math


def aufg1():

    intA = int(input("Wert A: "))
    intB = int(input("Wert B: "))

    while intA > 0 and intB > 0:

        if intA > intB:
            intA = intA - intB
        else:
            intB = intB - intA

    if intB == 0:
        print(str(intA) + " ist der ggT")
    else:
        print(str(intB) + " ist der ggT")


def aufg2():

    gefahreneKM = int(input("Geben sie die gefahrenen Km ein: "))
    preis = 0

    if gefahreneKM <= 6:
        preis = 17
    elif gefahreneKM <= 11:
        preis = 20
    elif gefahreneKM <= 19:
        preis = 25
    elif gefahreneKM <= 27:
        preis = 29
    else:
        preis = 32

    print("Erwachsene: " + str(preis * 10) + "Yen")
    print("Kinder: " + str(math.ceil(preis / 2) * 10) + "Yen")


def aufg3():

    längere = float(input("Bitte geben Sie die längere Seite in cm des Briefs ein: "))
    kürzere = float(input("Bitte geben Sie die kürzere Seite in cm des Briefs ein: "))
    gewicht = int(input("Bitte geben Sie das Gewicht in Gramm des Briefs an: "))

    if längere <= 23.5 and kürzere <= 12.5:

        if gewicht <= 20:
            print("Porto: 0,80€ (Standardbrief)")
        elif gewicht <= 50:
            print("Porto: 0,95€ (Kompaktbrief)")
        elif gewicht <= 500:
            print("Porto: 1,55€ (Großbrief)")
        elif gewicht <= 1000:
            print("Porto: 2,70€ (Maxibrief)")
        else:
            print("Brief zu schwer. Bitte als Paket versenden.")

    elif längere <= 35.3 and kürzere <= 25.0:

        if gewicht <= 500:
            print("Porto: 1,55€ (Großbrief)")
        elif gewicht <= 1000:
            print("Porto: 2,70€ (Maxibrief)")
        else:
            print("Brief zu schwer. Bitte als Paket versenden.")

    else:
        print("Brief zu groß. Bitte als Paket versenden.")
