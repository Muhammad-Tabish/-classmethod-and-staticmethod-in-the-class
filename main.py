class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
        return f"< FixedFloat {self.amount:.2f}>"

    @classmethod 
    def from_sum(cls,value1, value2):
        return cls (value1 + value2)    

new_number = FixedFloat.from_sum(19.58, 18.56)
print(new_number)

class dollar(FixedFloat):
    def __init__(self,amount):
     super().__init__(amount)
     self.symbol = '$'
    
    def __repr__(self):
        return f'<Dollar {self.symbol} {self.amount:.2f}>'

money = dollar.from_sum(18.56, 1956)
print(money)

        
