import math
class Fraction:
    def __init__(self, num, denum):
        self.num = num
        self.denum = denum
    def multiply(self, mult):
        temp = Fraction(1,1)
        temp.num = self.num * mult.num
        temp.denum = self.denum * mult.denum
        return temp
    def add (self, add):
        temp = Fraction(1,1)
        val = int (self.denum * add.denum / math.gcd(self.denum, add.denum))
        mult_num_1 = val / self.denum
        mult_num_2 = val / add.denum
        temp.num = int ( (self.num * mult_num_1) + (add.num * mult_num_2) )
        temp.denum = val
        return temp
    def sub (self, sub):
        temp = Fraction(1,1)
        val = int (self.denum * sub.denum / math.gcd(self.denum, sub.denum))
        mult_num_1 = val / self.denum
        mult_num_2 = val / sub.denum
        temp.num = int ( (self.num * mult_num_1) - (sub.num * mult_num_2) )
        temp.denum = val
        return temp  
    def div (self, div):
        temp = Fraction (1,1)
        temp.num = self.num * div.denum
        temp.denum = self.denum * div.num
        return temp      
    def set_reduce_fraction(self):
        nod = math.gcd(self.num,self.denum)
        self.num = int (self.num / nod)
        self.denum = int (self.denum / nod)
    def print_fraction (self):
        print ("{}/{}".format(self.num, self.denum))

r1 = Fraction(5,6)
r2 = Fraction(2,3)
r_mult = r1.multiply(r2)
r_mult.print_fraction()
r_add = r1.add(r2)
r_add.set_reduce_fraction()
r_add.print_fraction()
r_sub = r1.sub(r2)
r_sub.print_fraction()
r_div = r1.div(r2)
r_div.print_fraction()