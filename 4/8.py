def q8():
        num=int(input("Enter the value of number:"))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print("Factorial of a given number is",fact)
q8()