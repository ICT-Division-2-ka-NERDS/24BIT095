def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact 

n = int(input("Enter n: "))
r = int(input("Enter r: "))

nCr = factorial(n) // (factorial(r) * factorial(n - r))
nPr = factorial(n) // factorial(n - r)

print(n, "C", r, "=", nCr)
print(n, "P", r, "=", nPr)

