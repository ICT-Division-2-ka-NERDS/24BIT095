def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    return str(n) == str(n**2)[-len(str(n)):]

A = int(input("Enter a number: "))

print(f"{A} is a prime number: {is_prime(A)}")
print(f"{A} is a perfect number: {is_perfect(A)}")
print(f"{A} is an Armstrong number: {is_armstrong(A)}")
print(f"{A} is a palindrome: {is_palindrome(A)}")
print(f"{A} is an automorphic number: {is_automorphic(A)}") 