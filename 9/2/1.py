def prime_factors():
    
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5) + 1):  
            if n % i == 0:
                return False
        return True

    lst = []  

    def primeFactors(n: int, i=2):
        if n <= 1:  
            print(lst)
            return
        while n % i == 0:
            lst.append(i)
            n //= i  
        primeFactors(n, i + 1)  

    num = int(input("Enter a number: "))  
    primeFactors(num)

prime_factors()