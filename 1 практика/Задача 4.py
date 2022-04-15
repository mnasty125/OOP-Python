class Rectangle:
    def __init__ (self):
        self.lenght=1
        self.width=1
    def area (self):
        return self.lenght * self.width
    def perimeter (self):
        return  2*(self.lenght + self.width)
    def setlenght (self, new_lenght):
        self.lenght=new_lenght
    def setwidth (self, new_width):
        self.width=new_width

rect=Rectangle()
rect.setlenght(3)
rect.setwidth(2)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())



