from Beverage import Beverage
from Payment import PaymentSystem
from AdminMode import AdminMode

class VendingMachine:
    def __init__(self):
        self.beverages = {
            1: Beverage("콜라", 1800, 10),
            2: Beverage("환타", 1700, 10),
            3: Beverage("밀키스", 1900, 10),
            4: Beverage("사이다", 2000, 10)
        }
        self.ps = PaymentSystem(0)
        self.ad = AdminMode(self.beverages)

    def displayMenu(self):
        print("======= Menu ======")
        for number, beverage in self.beverages.items():
            print(f"{number}. {beverage.getName()} - {beverage.getPrice()}원 (재고: {beverage.getCount()}개)")
        print("999. 비밀번호 입력")

    def addMoney(self, amount):
        self.ps.add(amount)
        print(f"{amount}원이 추가되었습니다. 현재 잔액: {self.ps.amount}원")

    def purchaseBeverage(self, choice):
        if choice in self.beverages:
            selectedBeverage = self.beverages[choice]
            if selectedBeverage.getCount() > 0 and self.ps.amount >= selectedBeverage.getPrice():
                self.ps.deduct(selectedBeverage.getPrice())
                selectedBeverage.sale()
                print(f"{selectedBeverage.getName()}을(를) 구매했습니다. 남은 잔액: {self.ps.amount}원.")
            else:
                print("잔액이 부족하거나 음료가 품절되었습니다.")
        elif choice == 999:
            self.enterAdminMode()  # 999 입력 시 관리자 모드 접속 가능
        else:
            print("잘못된 선택입니다.")

    def enterAdminMode(self):
        password = input("비밀번호를 입력하세요: ")
        if self.ad.enterAdminMode(password): # 비밀번호 : 999
            print("관리자 모드에 접속했습니다.")