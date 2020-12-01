from numbers import Number
import math


class ComplexNumber:
    """поле комплексных чисел"""

    def __init__(self, values):
        if isinstance(values, Number):
            self.real = values
            self.imaginary = 0
        else:
            if isinstance(values, list) and len(values) == 2:
                if isinstance(values[0], Number) and isinstance(values[1], Number):
                    self.real = values[0]
                    self.imaginary = values[1]
                else:
                    raise ValueError("Impossible to create a complex number")
            else:
                raise ValueError("Impossible to create a complex number")
        
    def __str__(self):
        a, b = '',''
        if self.real != 0:
            a = str('{:.3f}'.format(self.real))
        if self.imaginary != 0:
            b = ('','+')[self.imaginary > 0] + str('{:.3f}'.format(self.imaginary)) + 'i'
        return a + b

    def absolute(self):
        return math.sqrt(self.real*self.real + self.imaginary*self.imaginary)

    def argument(self):
        return math.atan(self.imaginary / self.real)

    def conjugate(self):
        self.imaginary *= -1
        return self

    def __neg__(self):
        return ComplexNumber([
            -self.real, -self.imaginary 
            ])
    
    def __add__(self, other):
        if isinstance(other, ComplexNumber) == False:
            other = ComplexNumber(other)
        return ComplexNumber([
            self.real +  other.real, self.imaginary + other.imaginary 
            ])

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber) == False:
            other = ComplexNumber(other)
        return ComplexNumber([
            self.real*other.real - self.imaginary*other.imaginary, self.real*other.imaginary + self.imaginary*other.real
            ])
    
    def __rmul__(self, other):
        return self.__mul__(other)

c1 = ComplexNumber([3, 4])
c2 = ComplexNumber([2, 7.5])
print(c1)
print(-c2)
print(c1.absolute())
print(c1.argument())
print(c1+c2)
print([2,5]+c1)
print(c1.conjugate())

