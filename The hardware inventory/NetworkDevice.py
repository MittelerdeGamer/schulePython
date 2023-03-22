class NetworkDevice:

    __name: str
    __vendor: str
    __type: str
    __ip: str
    __numberOfPorts: int

    def __init__(self, name: str, vendor: str, typ: str, ip: str, numberOfPorts: int):
        self.__name = name
        self.__vendor = vendor
        self.__type = typ
        self.__ip = ip
        self.__numberOfPorts = numberOfPorts

    def printInformation(self):
        print(f"- Name: {self.__name}")
        print(f"- Vendor: {self.__vendor}")
        print(f"- Type: {self.__type}")
        print(f"- IP: {self.__ip}")
        print(f"- Number of Ports: {self.__numberOfPorts}")

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name
        
    def getIP(self) -> str:
        return self.__ip
    
    def setIP(self, IP: str):
        self.__ip = IP

    def getNumberOfPorts(self) -> int:
        return self.__numberOfPorts

    def setNumberOfPorts(self, NumberOfPorts: int):
        self.__numberOfPorts = NumberOfPorts
