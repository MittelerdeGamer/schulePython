def aufg1():
    vorherKm = float(input("Kilometerzähler beim letzten Tanken: "))
    liter = float(input("Getankte Menge in Liter: "))
    jetztKm = float(input("Kilometerzähler jetzt: "))
    print("Durchschnittsverbrauch: " + str(liter/((jetztKm-vorherKm)/100)) + "l/100km")


def aufg2():
    groese = float(input("Größe in cm: "))/100
    gewicht = float(input("Gewicht: "))
    bmi = gewicht/(groese*groese)
    if bmi <= 18.5:
        print("BMI: " + str(bmi) + "\nSie sind im Untergewicht.")
    elif bmi < 25:
        print("BMI: " + str(bmi) + "\nSie sind im Normalgewicht.")
    else:
        print("BMI: " + str(bmi) + "\nSie sind im Übergewicht.")