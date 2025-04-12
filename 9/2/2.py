def binary(n):
    
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binary(n // 2) + str(n % 2)

num = int(input("Enter a number: "))
print(binary(num))
print("Binary of", num, "is", binary(num))
