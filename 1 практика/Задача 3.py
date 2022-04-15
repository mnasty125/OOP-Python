class Car:
    def __init__ (self, color, tupe, year):
        self.color=color
        self.tupe=tupe
        self.year=year
    def start (self):
        return "Car start"
    def end (self):
        return "Car end"
    def setyear (self, new_year):
        self.year=new_year
    def getyear (self):
        return self.year
    def settupe (self, new_tupe):
        self.tupe=new_tupe
    def gettupe (self):
        return self.tupe
    def setcolor (self, new_color):
        self.color=new_color
    def getcolor (self):
        return self.color
    def getinform (self):
        return (self.color, self.tupe, self.year)

my_car=Car("Red", "BMW", 2019)
print("Start:", my_car.start())
print("End:", my_car.end())
my_car.setyear(2020)
print(my_car.getyear())
my_car.settupe("Wolk")
print(my_car.gettupe())
my_car.setcolor("Green")
print(my_car.getcolor())
print("All information:", my_car.getinform())

