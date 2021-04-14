from numbers import Number
import math


class ComplexNumber:
    """поле комплексных чисел"""

    def __init__(self, re, im = 0.0):
        if isinstance(re, Number) and isinstance(im, Number):
            self.real = re
            self.imaginary = im
        else:
            raise ValueError("Impossible to create a complex number")
        
    def __str__(self):
        a, b = '',''
        if self.real != 0:
            a = str('{:.3f}'.format(self.real))
        if self.imaginary != 0:
            b = ('','+')[self.imaginary > 0] + str('{:.3f}'.format(self.imaginary)) + 'i'
        return a + b

    def __abs__(self):
        return math.sqrt(self.real*self.real + self.imaginary*self.imaginary)

    def argument(self):
        return math.atan(self.imaginary / self.real)

    def conjugate(self):
        self.imaginary *= -1
        return self

    def __neg__(self):
        return ComplexNumber(
            -self.real, -self.imaginary 
            )
    
    def __add__(self, other):
        if isinstance(other, ComplexNumber) == False:
            other = ComplexNumber(other)
        return ComplexNumber(
            self.real +  other.real, self.imaginary + other.imaginary 
            )

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber) == False:
            other = ComplexNumber(other)
        return ComplexNumber(
            self.real*other.real - self.imaginary*other.imaginary, self.real*other.imaginary + self.imaginary*other.real
            )
    
    def __rmul__(self, other):
        return self.__mul__(other)

