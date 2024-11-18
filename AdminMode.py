
class AdminMode:
    def __init__(self, beverages):
        self.beverages = beverages
        self.adminPassword = "999"  # 비밀번호

    def enterAdminMode(self, password):
        if password == self.adminPassword:
            print("관리자 모드에 접속하셨습니다.")
            self.adminMenu()  # 관리자 메뉴로 이동
            return True
        else:
            print("비밀번호가 틀렸습니다.")
            return False

    def adminMenu(self):
        while True:
            print("======= Admin Mode =======")
            print("1. 음료 세팅")
            print("2. 판매 실적 확인")
            print("3. 판매 실적 초기화")
            print("0. 관리자 모드 종료")
            choice = int(input("메뉴를 선택하세요: "))

            if choice == 1:
                self.setBeverages()
            elif choice == 2:
                self.showSales()
            elif choice == 3:
                self.resetSales()
            elif choice == 0:
                print("관리자 모드를 종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")

    def setBeverages(self):
        print("\n음료 설정")
        for number, beverage in self.beverages.items():
            print(f"{number}. {beverage.getName()} - 현재 가격: {beverage.getPrice()}원, 재고: {beverage.getCount()}개")
            new_price = int(input(f"{beverage.getName()}의 새 가격을 입력하세요 (현재 {beverage.getPrice()}원): "))
            new_count = int(input(f"{beverage.getName()}의 새 재고 수량을 입력하세요 (현재 {beverage.getCount()}개): "))
            beverage.changePrice(new_price)
            beverage.changeCount(new_count)
        print("음료 설정이 완료되었습니다.")

    def showSales(self):
        print("\n판매 실적 확인")
        haveSales = False
        for number, beverage in self.beverages.items():
            if beverage.getSalesCount() > 0:
                print(f"{beverage.getName()} - 판매된 수량: {beverage.getSalesCount()}개")
                haveSales = True
        if not haveSales:
            print("판매된 음료가 없습니다.")

    def resetSales(self):
        print("\n판매 실적 초기화")
        for beverage in self.beverages.values():
            beverage.resetSalesCount()
        print("판매 실적이 초기화되었습니다.")