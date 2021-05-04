class Interval:
    def __init__(self, a, b, c, d, n):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.n = n
        
    def __addition__(self):
        return [self.a + self.c, self.b + self.d]
        
    def __subtraction__(self):
        return [self.a - self.d, self.b - self.c]
        
    def __division__(self):
        if (self.c == 0 or self.d == 0):
            print("Dividindo por zero") 
        else: 
            return [min(self.a/self.c, self.a/self.d, self.b/self.c, self.b/self.d), max(self.a/self.c, self.a/self.d, self.b/self.c, self.b/self.d)]
        
    def __multiplication__(self):
        return [min(self.a*self.c, self.a*self.d, self.b*self.c, self.b*self.d), max(self.a*self.c, self.a*self.d, self.b*self.c, self.b*self.d)]
        
    def __power__(self):
        return [self.a**self.n,self.b**self.n]
    
test = Interval(1,2,0,4,5)


print(test.__addition__())
print(test.__subtraction__())
print(test.__division__())
print(test.__multiplication__())
print(test.__power__())