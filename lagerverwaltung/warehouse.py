class Item:
    # TODO: Aufgabe 1
    __sku: str

    def __init__(self, sku: str):
        self.__sku = sku

    def getSKU(self) -> str:
        return self.__sku


class Shelf:
    __items: list
    __identifier: str

    def __init__(self, identifier: str):
        self.__identifier = identifier
        self.__items = []

    def addItem(self, item: Item) -> None:
        # TODO: Aufgabe 2
        self.__items.append(item)

    def getItems(self) -> list:
        return self.__items

    def getIdentifier(self) -> str:
        return self.__identifier


class Row:
    __shelves: list
    __identifier: str

    def __init__(self, identifier: str):
        self.__identifier = identifier
        self.__shelves = []

    def addShelf(self, shelf: Shelf) -> None:
        self.__shelves.append(shelf)

    def getIdentifier(self) -> str:
        return self.__identifier

    def getShelves(self) -> list:
        return self.__shelves


class Warehouse:
    __rows: list

    def __init__(self):
        self.__rows = []
        self.__create_storage()

    def __create_storage(self) -> None:
        # In diesem Beispiel erstellen wir ein Lager 
        # mit 3 Reihen á 10 Regalen
        for i in range(1, 4):
            r = Row(str(i))
            for j in range(1, 11):
                s = Shelf(str(j))
                r.addShelf(s)
            self.__rows.append(r)

    def store(self, sku: str, location: str) -> None:
        # TODO: Aufgabe 3
        try:
            row, shelve = location.split("-")  # Input "2-3" : row = "2", shelve = "3"
            row = int(row) - 1  # convert from 1,2,3,4... to 0,1,2,3...
            shelve = int(shelve) - 1  # convert from 1,2,3,4... to 0,1,2,3...
            self.__rows[row].getShelves()[shelve].addItem(Item(sku))
        except:
            raise Exception("Ungültiger Lagerplatz")

    def store_advanced(self, sku: str, location: str) -> bool:
        # TODO: Aufgabe 3
        try:
            row_identifier, shelve_identifier = location.split("-")  # Input "2-3" : row = "2", shelve = "3"
            for row in self.__rows:
                if row.getIdentifier() == row_identifier:
                    for shelve in row.getShelves():
                        if shelve.getIdentifier() == shelve_identifier:
                            shelve.addItem(Item(sku))
                            return True
            raise Exception("Lagerplatz nicht gefunden")
        except:
            raise Exception("Ungültiger Lagerplatz")

    def getOverview(self) -> str:
        # TODO: Aufgabe 4
        rvalue = "Reihe-Regal Items(SKUs)"
        for row in self.__rows:
            for shelve in row.getShelves():
                iStr = ""
                for item in shelve.getItems():
                    if len(iStr) > 0:
                        iStr = iStr + ", "
                    iStr = iStr + item.getSKU()
                if len(iStr) == 0:
                    iStr = "leer"
                rvalue = rvalue + "\n" + row.getIdentifier() + "-" + shelve.getIdentifier() + "\t" + iStr
        return rvalue

    def find(self, sku: str) -> str:
        # TODO: Aufgabe 5
        for row in self.__rows:
            for shelve in row.getShelves():
                for item in shelve.getItems():
                    if item.getSKU() == sku:
                        return row.getIdentifier() + "-" + shelve.getIdentifier()
        return "0"

    def retrieve(self, sku: str) -> None:
        # TODO: Aufgabe 6
        for row in self.__rows:
            for shelve in row.getShelves():
                for item in shelve.getItems():
                    if item.getSKU() == sku:
                        shelve.getItems().remove(item)
