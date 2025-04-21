class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def printComplex(self):
        print("Complex number:", self.real, "+", self.imag, "i")
    def addComplex(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def subComplex(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def mulComplex(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    def divComplex(self, other):
        denom = other.real * other.real + other.imag * other.imag
        return Complex((self.real * other.real + self.imag * other.imag) / denom, (self.imag * other.real - self.real * other.imag) / denom)    
        
ob1 = Complex(10, 20)
ob2 = Complex(30, 40)
ob1.printComplex()
ob2.printComplex()
print("Addition:")
ob1.addComplex(ob2).printComplex()
print("Subtraction:")
ob1.subComplex(ob2).printComplex()
print("Multiplication:")
ob1.mulComplex(ob2).printComplex()
print("Division:")
ob1.divComplex(ob2).printComplex()    