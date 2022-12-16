import subprocess


def readFile(datafile):
    # this is a basic funktion to read data from a file
    try:
        file = open(datafile, "r")
        data = file.read()
        file.close()
        return data
    except:
        exit("Error Die Datei konnte nicht geöfnet werden")


def ping(host):
    # this is a simplification of the ping process
    ping = subprocess.run(["ping", "-n", "1", host], stdout=subprocess.PIPE)
    if ping.returncode == 0:
        return True
    else:
        return False


def appendToFile(datafile, string):
    # this is a basic funktion to append data to a file
    try:
        file = open(datafile, 'a')
        file.write("\n" + string)
        file.close()
        return True
    except:
        return False


def writeToFile(datafile, string):
    # this is a basic funktion to overwrite a file
    try:
        file = open(datafile, 'w')
        file.write(string)
        file.close()
        return True
    except:
        return False


def ipListeAuflisten(datafile):
    # this funktion is just for displaying the content from the datafile
    data = readFile(datafile)
    print(data)


def ipHinzufuegen(datafile):
    # this funktion is for appending an IP-Address to the content of the datafile
    # get the IP-Address
    print("Welche IP soll hinzugefügt werden? \tz.B.: xxx.xxx.xxx.xxx oder google.com")
    ip = input("IP :")
    # add the IP-Address to the file and respond the result
    if appendToFile(datafile, ip):
        print("IP erfolgreich in die Datei geschrieben")
    else:
        print("Fehler beim schreiben in die Datei")


def ipEntfernen(datafile):
    # this funktion is for removing an IP-Address from the content of the datafile
    # get the IP-Address
    print("Welche IP soll entfernt werden? \tz.B.: xxx.xxx.xxx.xxx oder google.com")
    ip = input("IP :")
    data = readFile(datafile).split("\n")   # get the current data from the datafile and split it to a list
    counter = -1    # counter to count the removed IP-Address
    # this is the "stingFile" with the static IP-Address that will overwrite the current datafile
    stringFile = "127.0.0.1"
    for entry in data:
        # every line from the datafile is checked if it contains the IP-Address to remove
        if (entry == ip) or (entry == "127.0.0.1"):
            # to remove the IP-Address it is simply not added to the stringFile
            counter = counter + 1   # the counter is to count how often the IP-Address was present
        else:
            # write entry to stringFile
            stringFile = stringFile + "\n" + entry
    # write the stringFile to the datafile and respond the Result
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
    # this funktion is for pinging all IP-Addresses present in the datafile
    data = readFile(datafile).split("\n")   # get the content of the datafile and split it to a list
    # every IP from the datafile is pinged and respond the result
    for ip in data:
        if ping(ip):
            print("Der Ping für " + str(ip) + " war erfolgreich")
        else:
            print("Der Ping für " + str(ip) + " war nicht erfolgreich")


if __name__ == '__main__':
    # this is the Menu to select what you want to do
    print('\nPing-Test-Skript')
    datafile = "C:\\data\\hostliste.txt"    # this variable defines the file where the ip addresses are stored
    running = True  # this boolean is used to run the main menu and to exit it
    # this loop runs the main menu again after every function
    while (running):
        # this print() is displaying the funktion selection from a long string
        print("""
1\tIP-Liste auflisten
2\tIP hinzufügen
3\tIP entfernen
4\tPing-Test durchführen

0\tBeenden
""")
        select = input("Wähle eine Funktion aus: ")     # get the user input for selection
        # select the funktion which the user selected
        if select == "1":
            print("\nIP-Liste auflisten\n")
            ipListeAuflisten(datafile)
        elif select == "2":
            print("\nIP hinzufügen\n")
            ipHinzufuegen(datafile)
        elif select == "3":
            print("\nIP entfernen\n")
            ipEntfernen(datafile)
        elif select == "4":
            print("\nPing-Test durchführen\n")
            pingTest(datafile)
        elif select == "0":
            running = False
            print("\nProgramm wird beendet...")
        else:
            print("\n" + str(select) + " ist eine ungültige Eingabe!")
        print("\n--------------------------------")     # print a line to better split the actions
