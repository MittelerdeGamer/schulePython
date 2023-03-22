from NetworkDevice import NetworkDevice


class Switch(NetworkDevice):
    __sizeOfSAT: int

    def __init__(self, name: str, vendor: str, typ: str, ip: str, numberOfPorts: int, sizeOfSAT: int):
        super().__init__(name, vendor, typ, ip, numberOfPorts)
        self.__sizeOfSAT = sizeOfSAT

    def printInformation(self):
        super().printInformation()
        print(f"- Size of SAT: {self.__sizeOfSAT}")

    def getSizeOfSAT(self) -> int:
        return self.__sizeOfSAT

    def setSizeOfSAT(self, value: int):
        self.__sizeOfSAT = value
