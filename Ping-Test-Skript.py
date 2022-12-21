import datetime
import subprocess
import os
import time
import sys


def validate_ip(ipaddr):
    ip_sublist = ipaddr.split('.')
    if len(ip_sublist) != 4:
        return False
    for part in ip_sublist:
        if not part.isdigit():
            return False
        i = int(part)
        if i < 0 or i > 255:
            return False
    return True


def file_exists(exits_file):
    # this is a basic funktion to check if a file exists
    returnvalue = os.path.isfile(exits_file)
    time.sleep(1)
    return returnvalue


def read_file(read_datafile):
    # this is a basic funktion to read data from a file
    success = False
    count = 0
    data = ""
    while not success and count < 3:
        count = count + 1
        try:
            file = open(read_datafile, "r")
            data = file.read()
            file.close()
            success = True
        except:
            print("Die Datei " + read_datafile + " konnte nicht geöfnet werden\nErneuter Versuch in 3 sec")
            time.sleep(3)
    if success:
        return data
    else:
        exit("Abbrechen Die Datei " + read_datafile + " konnte nicht geöfnet werden")


def is_valid_file(valid_datafile):
    # this is a basic funktion to check if a file is valid
    data = read_file(valid_datafile).splitlines()
    for ip in data:
        if not validate_ip(ip):
            return False
    return True


def ping(host):
    # this is a simplification of the ping process
    ping = subprocess.run(["ping", "-n", "1", host], stdout=subprocess.PIPE)
    if ping.returncode == 0:
        return True
    else:
        return False


def append_to_file(append_datafile, string):
    # this is a basic funktion to append data to a file
    try:
        file = open(append_datafile, 'a')
        file.write("\n" + string)
        file.close()
        return True
    except:
        return False


def write_to_file(write_datafile, string):
    # this is a basic funktion to overwrite a file
    try:
        file = open(write_datafile, 'w')
        file.write(string)
        file.close()
        return True
    except:
        return False


def ip_liste_auflisten(liste_datafile):
    # this funktion is just for displaying the content from the datafile
    data = read_file(liste_datafile)
    print(data)


def ip_hinzufuegen(hinzufuegen_datafile):
    # this funktion is for appending an IP-Address to the content of the datafile
    # get the IP-Address
    valid_ip = False
    ip = ""
    while not valid_ip:
        print("Welche IP soll hinzugefügt werden? \tz.B.: xxx.xxx.xxx.xxx oder google.com")
        ip = input("IP :")
        if validate_ip(ip):
            valid_ip = True
        else:
            print("Die eingegebene IP-Adresse: ", ip, " ist ungültig")
    # add the IP-Address to the file and respond the result
    if append_to_file(hinzufuegen_datafile, ip):
        print("IP erfolgreich in die Datei geschrieben")
    else:
        print("Fehler beim schreiben in die Datei")


def ip_entfernen(entfernen_datafile):
    # this funktion is for removing an IP-Address from the content of the datafile
    # get the IP-Address
    print("Welche IP soll entfernt werden? \tz.B.: xxx.xxx.xxx.xxx oder google.com")
    ip = input("IP :")
    data = read_file(entfernen_datafile).splitlines()  # get the current data from the datafile and split it to a list
    counter = -1  # counter to count the removed IP-Address
    # this is the "stingFile" with the static IP-Address that will overwrite the current datafile
    stringFile = "127.0.0.1"
    for entry in data:
        # every line from the datafile is checked if it contains the IP-Address to remove
        if (entry == ip) or (entry == "127.0.0.1"):
            # to remove the IP-Address it is simply not added to the stringFile
            counter = counter + 1  # the counter is to count how often the IP-Address was present
        else:
            # write entry to stringFile
            stringFile = stringFile + "\n" + entry
    # write the stringFile to the datafile and respond the Result
    if write_to_file(entfernen_datafile, stringFile):
        if counter < 0:
            print("etwas ist schief gelaufen")
        elif counter == 0:
            print("Die IP: " + ip + " wurde nicht gefunden")
        else:
            print("Die IP: " + ip + " wurde " + str(counter) + " mal gefunden und entfernt")
    else:
        print("Fehler beim schreiben in die Datei")


def ping_test(ping_datafile):
    # this funktion is for pinging all IP-Addresses present in the datafile
    data = read_file(ping_datafile).splitlines()  # get the content of the datafile and split it to a list
    # every IP from the datafile is pinged and respond the result
    for ip in data:
        timestamp = datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")
        if ping(ip):
            print(timestamp, "Der Ping für " + str(ip) + " war erfolgreich")
        else:
            print(timestamp, "Der Ping für " + str(ip) + " war nicht erfolgreich")


def main_menu(menu_datafile):
    # this is the Menu to select what you want to do
    # menu_datafile defines the file where the ip addresses are stored
    print("\n--------------------------------")
    print('\nPing-Test-Skript-Menu')
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
        select = input("Wähle eine Funktion aus: ")  # get the user input for selection
        # select the funktion which the user selected
        if select == "1":
            print("\nIP-Liste auflisten\n")
            ip_liste_auflisten(menu_datafile)
        elif select == "2":
            print("\nIP hinzufügen\n")
            ip_hinzufuegen(menu_datafile)
        elif select == "3":
            print("\nIP entfernen\n")
            ip_entfernen(menu_datafile)
        elif select == "4":
            print("\nPing-Test durchführen\n")
            ping_test(menu_datafile)
        elif select == "0":
            running = False
            print("\nMenu wird beendet...")
        else:
            print("\n" + str(select) + " ist eine ungültige Eingabe!")
        print("\n--------------------------------")  # print a line to better split the actions


def file_select():
    print("\nIP-Datei auswählen")
    file_found = False
    inputfile = ""
    while not file_found:
        print("""
    1\tIP-Datei auswählen
    2\tIP-Datei erstellen

    0\tBeenden
        """)
        select = input("Wähle eine Funktion aus: ")  # get the user input for selection
        # select the funktion which the user selected
        if select == "1":
            print("\nIP-Datei auswählen\n")
            inputfile = input("Bitte geben sie den Pfad zur Datei an: ")
            if file_exists(inputfile):
                print("Datei", inputfile, " wird ausgewählt")
                if not is_valid_file(inputfile):
                    print("Die Datei enthält ungültige IP-Adressen")
                file_found = True
            else:
                print("Die Datei ", inputfile, " existiert nicht")
        elif select == "2":
            print("\nIP-Datei erstellen\n")
            inputfile = input("Bitte geben sie den Pfad zur Datei an: ")  # .replace("\n", "\\n").replace("\t", "\\t")
            # inputfile.replace("\r", "\\r").replace("\b", "\\b").replace("\f", "\\f")
            if file_exists(inputfile):
                print("Overwriting file: ", inputfile)
            if write_to_file(inputfile, "127.0.0.1"):
                print("IP Datei erfolgreich erstellt")
                file_found = True
            else:
                print("Fehler beim schreiben in die Datei")
        elif select == "0":
            exit("\nPing-Test-Skript wird beendet...")
        else:
            print("\n" + str(select) + " ist eine ungültige Eingabe!")
        print("\n--------------------------------")  # print a line to better split the actions
    return inputfile


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if file_exists(sys.argv[1]):
            print("Automated Ping Process")
    else:
        print('\nPing-Test-Skript')
        datafile = file_select()
        main_menu(datafile)
