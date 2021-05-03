class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def simplify(self):
        a = self.numerator / self.denominator
        return a.as_integer_ratio()
    

q = RationalNumber(1100,50)

print(q.simplify())