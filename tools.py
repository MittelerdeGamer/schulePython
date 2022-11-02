def iptranslator():
    print("\n\t1: IPv4 to binary \n\t2: binary to IPv4 "
          "\n\t3: IPv6 to binary \n\t4: binary to IPv6 "
          "\n\n\tNote: always input delimiter and putt 0 between if empty \n")
    mode = int(input("Select Mode: "))
    print()

    if mode == 1:

        ipv4 = input("IPv4: ")
        iparr = ipv4.split('.')
        print("binary: " + format(int(iparr[0]), "08b") + "." + format(int(iparr[1]), "08b") + "." +
              format(int(iparr[2]), "08b") + "." + format(int(iparr[3]), "08b"))

    elif mode == 2:

        binary = input("binary: ")
        binaryarr = binary.split('.')
        print("IPv4: " + str(int(binaryarr[0], 2)) + "." + str(int(binaryarr[1], 2)) + "." +
              str(int(binaryarr[2], 2)) + "." + str(int(binaryarr[3], 2)))

    elif mode == 3:

        ipv6 = input("IPv6: ")
        iparr = ipv6.split(':')
        print("binary: " + format(int(iparr[0], 16), "016b") + ":" + format(int(iparr[1], 16), "016b") + ":" +
              format(int(iparr[2], 16), "016b") + ":" + format(int(iparr[3], 16), "016b") + ":" +
              format(int(iparr[4], 16), "016b") + ":" + format(int(iparr[5], 16), "016b") + ":" +
              format(int(iparr[6], 16), "016b") + ":" + format(int(iparr[7], 16), "016b"))

    elif mode == 4:

        binary = input("binary: ")
        binaryarr = binary.split(':')
        print("IPv6: " + format(int(binaryarr[0], 2), "04x") + ":" + format(int(binaryarr[1], 2), "04x") + ":" +
              format(int(binaryarr[2], 2), "04x") + ":" + format(int(binaryarr[3], 2), "04x") + ":" +
              format(int(binaryarr[4], 2), "04x") + ":" + format(int(binaryarr[5], 2), "04x") + ":" +
              format(int(binaryarr[6], 2), "04x") + ":" + format(int(binaryarr[7], 2), "04x"))

    else:

        print("Error \n mode out of bounds")


def hex2bin():
    print("\n\t1: Hex to binary \n\t2: binary to Hex \n")
    mode = int(input("Select Mode: "))
    print()

    if mode == 1:

        hexinput = input("Hex: ")
        print("binary: " + format(int(hexinput, 16), "0b"))

    elif mode == 2:

        binary = input("binary: ")
        print("Hex: " + format(int(binary, 2), "0x"))

    else:

        print("Error \n mode out of bounds")


def fakultaet(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def fakultaetBAD(n):
    if n == 1:
        return 1
    else:
        return n * fakultaetBAD(n-1)
