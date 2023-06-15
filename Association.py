class Customer:
    __nr: int
    __name: str
    __contractList: list

    def __init__(self, nr: int, name: str):
        self.__nr = nr
        self.__name = name
        self.__contractList = []

    def createContract(self, anr: int, description: str):
        self.__contractList.append(Contract(self, anr, description))

    def printContracts(self):
        printStr = f"\nContracts from {self.__name}({self.__nr})\n\n"
        if len(self.__contractList) == 0:
            printStr = printStr + f"No contracts available"
        else:
            printStr = printStr + f"Anr\t| Description\n"
            for c in self.__contractList:
                printStr = printStr+f"{c.getAnr()}\t| {c.getDescription()}\n"
        print(printStr)


class Contract:
    __customer: Customer
    __anr: int
    __description: str

    def __init__(self, customer: Customer, anr: int, description: str):
        self.__customer = customer
        self.__anr = anr
        self.__description = description

    def getAnr(self):
        return self.__anr

    def getDescription(self):
        return self.__description

    def getCustomer(self):
        return self.__customer


if __name__ == "__main__":
    c1 = Customer(1, "Muster")
    c1.printContracts()
    c1.createContract(2, "Monatliche 1Std Server Updates")
    c1.createContract(998, "Upgrade von Fritz Wlan zu Unifi Wlan")
    c1.createContract(1021, "Problem mit Netzwerk in Geb. 2 beheben")
    c1.printContracts()
