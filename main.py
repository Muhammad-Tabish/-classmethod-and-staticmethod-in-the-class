class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
        return f"< FixedFloat {self.amount:.2f}>"
number = FixedFloat(18.5888)
print(number)
