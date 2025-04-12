def power(**kwargs):
    
    a = kwargs.get('a')
    b = kwargs.get('b')
    
    if b == 0:
        return 1
    return a * power(a=a, b=b-1)

result = power(a=4, b=5) 
print("Result:", result)