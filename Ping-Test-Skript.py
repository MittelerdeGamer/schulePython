import subprocess


def readFile(datafile):
    try:
        file = open(datafile, "r")
        data = file.read()
        file.close()
        return data
    except:
        exit("Error Die Datei konnte nicht geöfnet werden")


def ping(host):
    ping = subprocess.run(["ping", "-n", "1", host], stdout=subprocess.PIPE)
    if ping.returncode == 0:
        return True
    else:
        return False


def ipListeAuflisten():
    data = readFile("C:\data\hostliste.txt")
    print(data)


def pingTest():
    data = readFile("C:\data\hostliste.txt")
    data = data.split("\n")
    for ip in data:
        if ping(ip) == True:
            print("Der Ping für " + str(ip) + " war erfolgreich")
        else:
            print("Der Ping für " + str(ip) + " war nicht erfolgreich")


if __name__ == '__main__':
    print('Ping-Test-Skript')
    running = True
    while (running):
        print("""
1\tIP-Liste auflisten
2\tIP hinzufügen
3\tIP entfernen
4\tPing-Test durchführen

0\tBeenden""")
        select = int(input())

        if select == 1:
            print("IP-Liste auflisten")
            ipListeAuflisten()
        elif select == 2:
            print("2")
        elif select == 3:
            print("3")
        elif select == 4:
            print("Ping-Test durchführen")
            pingTest()
        elif select == 0:
            running = False
        else:
            print(str(select) + " ist eine ungültige Eingabe!\n--------------------------------")
