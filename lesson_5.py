class Money:
    def __init__(self, amount=0):
        self.amount = amount

    def __str__(self):
        return f"экземпляр Money: {self.amount}"

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        pass

denshik_money = Money(667)
print(denshik_money)
isken_money = Money(228)
total_money = isken_money + denshik_money
print(total_money)
