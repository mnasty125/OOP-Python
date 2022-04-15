import math
class Trapezoid:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
        self.num2 = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
        self.c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        self.d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
    
    def proverka(self):
        if self.d == self.c:
            return True
        else:
            return False
    
        
    def side(self):
          print("Length of sides: " + "\nAB: ", self.a, "\nBC: ", self.c, "\nCD: ", self.d, "\nAD: ", self.num2)
        
    def perimeter(self):
        return self.a + self.num2 + self.c + self.d
    
    def area(self):
        return((self.a+self.num2)/2)*(math.sqrt((self.c**2)-((((self.num2-self.a)**2)+(self.c**2)-(self.d**2))/(2*(self.num2-self.a)))))
    
    def area_1(self):
        parim=self.perimeter()/2 
        return math.sqrt((parim-self.a)*(parim-self.num2)*(parim-self.c)*(parim-self.d) )


    
trap = Trapezoid(1,1,2,4,5,4,6,1)
trap.proverka()
trap.side()
if trap.proverka():
    print("Perimeter: %.2f " %trap.perimeter())
    print("Area: %.2f " %trap.area())
    print("Area: %.2f " %trap.area_1())
else:
    print("Unequal")