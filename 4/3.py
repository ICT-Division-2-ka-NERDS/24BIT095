A = input("Enter a string: ")

num_alphabets = sum(c.isalpha() for c in A)
num_digits = sum(c.isdigit() for c in A)

print("Number of alphabets:",num_alphabets)
print("Number of digits:",num_digits)