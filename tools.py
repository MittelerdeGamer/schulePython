def iptranslator():

    print("\n\t1: IPv4 to binary \n\t2: binary to IPv4 "
          "\n\t3: IPv6 to binary \n\t4: binary to IPv6 "
          "\n\n\tNote: always input delimiter and putt 0 between if empty \n")
    mode = int(input("Select Mode: "))
    print()

    if mode == 1:

        ipv4 = input("IPv4: ")
        iparr = ipv4.split('.')
        print(format(int(iparr[0]), "08b") + ":" + format(int(iparr[1]), "08b") + ":" +
              format(int(iparr[2]), "08b") + ":" + format(int(iparr[3]), "08b"))

    elif mode == 2:

        binary = input("binary: ")
        binaryarr = binary.split('.')
        print(str(int(binaryarr[0], 2)) + "." + str(int(binaryarr[1], 2)) + "." +
              str(int(binaryarr[2], 2)) + "." + str(int(binaryarr[3], 2)))

    elif mode == 3:

        ipv6 = input("IPv6: ")
        iparr = ipv6.split(':')
        print(format(int(iparr[0], 16), "016b") + ":" + format(int(iparr[1], 16), "016b") + ":" +
              format(int(iparr[2], 16), "016b") + ":" + format(int(iparr[3], 16), "016b") + ":" +
              format(int(iparr[4], 16), "016b") + ":" + format(int(iparr[5], 16), "016b") + ":" +
              format(int(iparr[6], 16), "016b") + ":" + format(int(iparr[7], 16), "016b"))
        # 2001:0db8:
        # 3c4d:0015:
        # 0000:0000:
        # 1a2f:1a2b
        # 0010000000000001:0000110110111000:0011110001001101:0000000000010101:0000000000000000:0000000000000000:0001101000101111:0001101000101011

    elif mode == 4:

        binary = input("binary: ")
        binaryarr = binary.split(':')
        print(format(int(binaryarr[0], 2), "04x") + ":" + format(int(binaryarr[1], 2), "04x") + ":" +
              format(int(binaryarr[2], 2), "04x") + ":" + format(int(binaryarr[3], 2), "04x") + ":" +
              format(int(binaryarr[4], 2), "04x") + ":" + format(int(binaryarr[5], 2), "04x") + ":" +
              format(int(binaryarr[6], 2), "04x") + ":" + format(int(binaryarr[7], 2), "04x"))

    else:

        print("Error \n mode out of bounds")
