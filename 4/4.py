A = int(input('Enter a Number:'))

prime = 0
for i in range(2,A):
    if A%i==0:
        prime+=1
if prime==0:
    print('Yes,its a prime number')
else:
    print('No,its not a prime number')

perfect = 0
for i in range(1,A):
    if A%i==0:
        perfect+=i    
if perfect==A:
    print('Yes,its a perfect number')
else:
    print('No,its not a perfect number')

armstrong = 0
length = len(str(A))
B = str(A)
for i in B:
    armstrong+=int(i)**length
if armstrong==A:
    print('Yes,its a armstrong number')
else:
    print('No,its not a armstrong number')

palindrome = 0
C = str(A)
if C==C[::-1]:
    print('Yes,its a palindrome number')
else:
    print('No,its not a palindrome number')

square = A*A
if square%(10**len(str(A)))==A:
    print('Yes,its a automorphic number')
else:
    print('No,its not a automorphic')
