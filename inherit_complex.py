#write a class complex to represent complex numbers, along with overloaded operators + and * which adds and multiplies them.

class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i

    def __add__(self,c):
        return Complex(self.real + c.real , self.imaginary + c.imaginary)

    def __mul__(self,c):
        mulreal = self.real*c.real - self.imaginary*c.imaginary
        mulimag = self.real*c.imaginary + c.real*self.imaginary
        return Complex(mulreal,mulimag)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(1,4)
c2 = Complex(8,5)
print(c1+c2)
print(c1*c2)
