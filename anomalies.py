# Jannis Swientek as Driver
# Max Melia Klüber as Navigator
import json


def main():
    # Aufgabe 2
    with open('anomalies.json', 'r') as file:
        anomalies = json.load(file)

    # Aufgabe 3
    # print(anomalies)

    # Aufgabe 4
    # print(f"Titel: {anomalies['description']}")

    # Aufgabe 5
    # print("Jahr / Anomalie")
    # for year, anomalie in anomalies["data"].items():
    #     print(f"{year} / {anomalie}")

    # Aufgabe 6
    # for year, anomalie in anomalies["data"].items():
    #     if 2000 <= int(year) <= 2016:
    #         print(f"{year} / {anomalie}")

    # Aufgabe 7
    # maxAnomalie = max(anomalies["data"], key=lambda k: anomalies["data"][k])
    # print(f"{maxAnomalie} war die höchste Anomalie mit {anomalies['data'][maxAnomalie]}")

    # Aufgabe 9
    anomalies["data"][2017] = "0,95"
    anomalies["data"][2018] = "0,9"
    anomalies["data"][2019] = "0,96"
    anomalies["data"][2020] = "1,1"
    anomalies["data"][2021] = "0,94"

    # Aufgabe 10
    with open('anomalies2.json', 'w') as file:
        json.dump(anomalies, file)


if __name__ == '__main__':
    main()
