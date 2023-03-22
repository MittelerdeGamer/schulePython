from Router import Router
from Switch import Switch


def main():
    s1 = Switch("sw-etage1-01", "Cisco", "SG500X", "192.168.0.11", 28, 4096)
    r1 = Router("ro-etage1-01", "HP", "MSR2003", "192.168.0.1", 2, 4096)
    print("Switch")
    s1.printInformation()
    print("Router")
    r1.printInformation()


if __name__ == "__main__":
    main()
