
class PaymentSystem:
    def __init__(self, amount=0):
        self.amount = amount

    def add(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            print("잘못된 금액을 입력하였습니다.")

    def deduct(self, amount):
        if self.amount >= amount:
            self.amount -= amount
        else:
            print("잔액이 부족합니다.")