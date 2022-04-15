class Triangle:
    def __init__ (self):
        self.side_1=1
        self.side_2=1
        self.side_3=1
    def test (self):
        if ( ((self.side_1 + self.side_2)>self.side_3) & ((self.side_3 + self.side_2)>self.side_1) & ((self.side_1 + self.side_3)>self.side_2) ):
            return True
        else:
            return False
    def setside_1 (self, new_side_1):
        self.side_1=new_side_1
    def setside_2 (self, new_side_2):
        self.side_2=new_side_2
    def setside_3 (self, new_side_3):
        self.side_3=new_side_3
    def perimeter (self):
        perimeter=self.side_1 + self.side_2 + self.side_3
        return perimeter
    def area (self) :
        perimeter=self.perimeter()
        per=perimeter/2
        area=(per*(per-self.side_1)*(per-self.side_2)*(per-self.side_3))**(1/2)
        return area

triang=Triangle()
triang.setside_1(3)
triang.setside_2(4)
triang.setside_3(5)
print("Test:", triang.test())
if triang.test():
    print("Perimeter:", triang.perimeter())
    print("Area:", triang.area())
else:
    print ("No, triangle does not exist")

