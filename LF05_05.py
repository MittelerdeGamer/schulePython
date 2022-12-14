import sys


def aufg1(datafile, index):

    try:
        file = open(datafile,"r")
        text = file.read()
        file.close()

        text = text.replace(",",".")
        lines = text.split("\n")
        line = lines[1].split(";")

        datarowname = lines[0].split(";")[index]   # Den Name der Spalte holen
        max = float(line[index])    #
        min = float(line[index])    # Initiales lesen der ersten Datenzeile
        total = float(line[index])  #
        count = 1                   #

        for i in range(2,len(lines)):
            line=lines[i].split(";")
            if line[index] == "-":
                continue
            temp = float(line[index])
            if max<temp:
                max = temp
            elif min>temp:
                min = temp
            total += temp
            count += 1
        average = total/count

        print(datarowname,": ")
        print("Maximalwert: ",max)
        print("Minimalwert: ",min)
        print("Durchschnittswert: ",average)
        print()
    except IOError:
        print("Datei kann nicht geöffnet werden",sys.exc_info()[0])
    except:
        print("Es ist folgender Fehler aufgetreten:",sys.exc_info()[0])

def aufg2(datafile, range):
    for i in range:
        aufg1(datafile, i)