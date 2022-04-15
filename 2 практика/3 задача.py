class Complex ():
    def __init__ (self,  real, imag):
        self.real = real
        self.imag = imag
    def __str__(self):
        if (self.imag >= 0):
            cont = '+'  
        else: 
            cont = ''
        return '{}{}{}i'.format(self.real, cont, self.imag)
class ComplexCalc():
    def add(self, c1, c2):
        real = c1.real + c2.real
        imag = c1.imag + c2.imag
        print (Complex(real, imag))
    def sub(self, c1, c2):
        real = c1.real - c2.real
        imag = c1.imag - c2.imag
        print (Complex(real, imag))
    def mul(self, c1, c2):
        real = c1.real * c2.real - c1.imag * c2.imag
        imag = c1.imag * c2.real + c1.real * c2.imag
        print (Complex(real, imag))
temp = ComplexCalc()
temp.add(Complex(1, 2), Complex(3, 4))
temp.sub(Complex(1, 2), Complex(3, 4))
temp.mul(Complex(1, 2), Complex(3, 4))