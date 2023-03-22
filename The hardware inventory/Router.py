from NetworkDevice import NetworkDevice


class Router(NetworkDevice):
    __sizeOfRoutingTable: int

    def __init__(self, name: str, vendor: str, typ: str, ip: str, numberOfPorts: int, sizeOfRoutingTable: int):
        super().__init__(name, vendor, typ, ip, numberOfPorts)
        self.__sizeOfRoutingTable = sizeOfRoutingTable

    def printInformation(self):
        super().printInformation()
        print(f"- Size of routing Table: {self.__sizeOfRoutingTable}")

    def getSizeOfRoutingTable(self) -> int:
        return self.__sizeOfRoutingTable

    def setSizeOfRoutingTable(self, value: int):
        self.__sizeOfRoutingTable = value
