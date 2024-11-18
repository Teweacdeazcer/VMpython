from VendingMachine import VendingMachine

if __name__ == "__main__":
    VM = VendingMachine()
    VM.displayMenu()
    amount = int(input("돈 입력(정수만 입력가능): "))
    VM.addMoney(amount)

    while True:
        choice = int(input("구매할 음료 번호를 입력하세요 (종료하려면 0을 입력): "))
        if choice == 0:
            print("자판기를 종료합니다.")
            break
        VM.purchaseBeverage(choice)
        VM.displayMenu()