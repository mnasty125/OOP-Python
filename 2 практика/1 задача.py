import math
class Fraction():
    def __init__(self, num_1, num_2):
        self.num_1=num_1
        self.num_2=num_2

    def drob(self):
        if ((self.num_1 > self.num_2) and (self.num_1 % self.num_2==0)):
            self.num_1 = int(self.num_1 / self.num_2)
            if (self.num_2 % self.num_1==0):
                self.num_2 = int(self.num_2 / self.num_1)
            else:
                self.num_2 = 1
        elif ((self.num_2 > self.num_1) and (self.num_2 % self.num_1==0)):
            self.num_2 = int(self.num_2 / self.num_1)
            if (self.num_1 % self.num_2==0):
                self.num_1 = int(self.num_1 / self.num_2)
            else:
                self.num_1 = 1
    
    def mult(self, num_3):
        self.num_1 = self.num_1 * num_3

    def div(self, num_4):
        self.num_2 = self.num_2 * num_4
    
fract=Fraction(3, 6)
fract.drob()
print("{}/{}". format(fract.num_1, fract.num_2))
fract.mult(5)
print("{}/{}". format(fract.num_1, fract.num_2))
fract.div(3)
fract.drob()
print("{}/{}". format(fract.num_1, fract.num_2))