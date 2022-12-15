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


def appendToFile(datafile, string):
    try:
        file = open(datafile, 'a')
        file.write("\n" + string)
        file.close()
        return True
    except:
        return False


def writeToFile(datafile, string):
    try:
        file = open(datafile, 'w')
        file.write(string)
        file.close()
        return True
    except:
        return False


def ipListeAuflisten(datafile):
    data = readFile(datafile)
    print(data)


def ipHinzufügen(datafile):
    print("Welche IP soll hinzugefügt werden? \tz.B.: xxx.xxx.xxx.xxx oder google.com")
    ip = input("IP :")
    if appendToFile(datafile, ip):
        print("IP erfolgreich in die Datei geschrieben")
    else:
        print("Fehler beim schreiben in die Datei")


def ipEntfernen(datafile):
    print("Welche IP soll entfernt werden? \tz.B.: xxx.xxx.xxx.xxx oder google.com")
    ip = input("IP :")
    data = readFile(datafile).split("\n")
    counter = -1
    stringFile = "127.0.0.1"
    for entry in data:
        if (entry == ip) or (entry == "127.0.0.1"):
            counter = counter + 1
        else:
            # write back to stringFile
            stringFile = stringFile + "\n" + entry
    if writeToFile(datafile, stringFile):
        if counter < 0:
            print("etwas ist schief gelaufen")
        elif counter == 0:
            print("Die IP: " + ip + " wurde nicht gefunden")
        else:
            print("Die IP: " + ip + " wurde " + str(counter) + " mal gefunden und entfernt")
    else:
        print("Fehler beim schreiben in die Datei")


def pingTest(datafile):
    data = readFile(datafile)
    data = data.split("\n")
    for ip in data:
        if ping(ip) == True:
            print("Der Ping für " + str(ip) + " war erfolgreich")
        else:
            print("Der Ping für " + str(ip) + " war nicht erfolgreich")


if __name__ == '__main__':
    print('\nPing-Test-Skript')
    datafile = "C:\data\hostliste.txt"
    running = True
    while (running):
        print("""
1\tIP-Liste auflisten
2\tIP hinzufügen
3\tIP entfernen
4\tPing-Test durchführen

0\tBeenden""")
        print()
        select = int(input("Wähle eine Funktion aus: "))
        print()

        if select == 1:
            print("IP-Liste auflisten\n")
            ipListeAuflisten(datafile)
        elif select == 2:
            print("IP hinzufügen\n")
            ipHinzufügen(datafile)
        elif select == 3:
            print("IP entfernen\n")
            ipEntfernen(datafile)
        elif select == 4:
            print("Ping-Test durchführen\n")
            pingTest(datafile)
        elif select == 0:
            running = False
            exit()
        else:
            print(str(select) + " ist eine ungültige Eingabe!")
        print("\n--------------------------------")
