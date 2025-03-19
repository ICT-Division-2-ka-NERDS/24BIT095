def q11():
    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    x = float(input("Enter x (in radians): "))
    sin_x = 0
    terms = 10  
    for i in range(terms):
        power = 2 * i + 1
        sign = (-1) ** i
        sin_x += sign * (x ** power) / factorial(power)
    
    print("sin(x) =", sin_x)

q11()