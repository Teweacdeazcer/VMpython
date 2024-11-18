
class Beverage:
    def __init__(self, name, price, count):
        self.__name = name
        self.__price = price
        self.__count = count
        self.__salesCount = 0

    def changeName(self, name):
        self.__name = name

    def changePrice(self, price):
        self.__price = price

    def changeCount(self, count):
        self.__count = count

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getCount(self):
        return self.__count

    def sale(self):
        if self.__count > 0:
            self.__count -= 1
            self.__salesCount += 1
        else:
            print("유효한 입력이 아닙니다.")

    def resetSalesCount(self):
        self.__salesCount = 0

    def getSalesCount(self):
        return self.__salesCount