def average_recursive(lst, n=None, total=0):
    
    if n is None:
        n = len(lst)
    
    if not lst:
        return total / n if n > 0 else 0 
    
    return average_recursive(lst[1:], n, total + lst[0])

numbers = [5, 10, 15, 20, 25]
average = average_recursive(numbers)
print("List of numbers:", numbers)
print("Average:", average)