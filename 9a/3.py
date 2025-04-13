import random

def generate_and_square():
    
    random_numbers = random.sample(range(-15, 16), 10)
    print("Original list of random numbers:", random_numbers)
    
    squared_numbers = list(map(lambda x: x**2, random_numbers))
    print("List of squared numbers:", squared_numbers)

generate_and_square()