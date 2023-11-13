def tupels():
    print("Aufgabe 1")
    vegetables = ("Brokkoli", "Spinat", "Chinakohl", "Petersilie", "Sprossen")
    print("Aufgabe 2")
    print(vegetables[-1])
    print("Aufgabe 3")
    print(vegetables.__sizeof__())
    print("Aufgabe 4")
    # TODO: Was? das geht nicht.
    print("Aufgabe 5")
    zahlen = (12, 5, 8, 7, 3, 7, 6, 4, 18)
    print("Aufgabe 6")
    for number in zahlen:
        if number % 2 == 0:
            print(number)
    print("Aufgabe 7")
    bigest = zahlen[0]
    for number in zahlen:
        if number > bigest:
            bigest = number
    print(bigest)
    print("Aufgabe 8")


def dicts():
    print("Aufgabe 1")
    car = {
        "manufacturer": "Volkswagen",
        "model": "Golf 8",
        "color": "rot",
        "km": 50000,
        "top_speed": 220,
        "previous_owners": ["Herr Klein", "Herr Dawadi", "Herr Kahl"]
    }
    print("Aufgabe 2")
    print(car["top_speed"])
    print("Aufgabe 3")
    print(car.keys())
    print("Aufgabe 4")
    print(car.values())
    print("Aufgabe 5")
    car["color"] = "grün"
    print("Aufgabe 6")
    car.pop("color")
    print("Aufgabe 7")
    car["previous_owners"].append("Frau Meier")
    print("Aufgabe 8")
    for key in car:
        print(key)
        print(car[key])


def main():
    tupels()
    dicts()


if __name__ == '__main__':
    main()
