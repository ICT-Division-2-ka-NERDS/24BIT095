A = input('Enter the first string:')
B = input('Enter the second string:')
if A.find(B):
    print(A.replace(B,''))
else:
    print('No')
