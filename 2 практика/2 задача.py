import math
class Circle():
    def __init__ (self, rad):
        self.rad=rad
     
    def circumference(self):
        return 2 * math.pi * self.rad
    
    def area(self):
        return math.pi * self.rad ** 2

circle=Circle(10)
print("Circumference: %.2f" %circle.circumference())
print("Area: %.2f" %circle.area())