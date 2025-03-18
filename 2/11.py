X1,X2,X3 = map(int, input("Enter X coordinates :").split())
Y1,Y2,Y3 = map(int, input('Enter Y coordinates :').split())
A = Y2 - Y1/X2 - X1
B = Y3 - Y2/X3 - X2
if A == B:
    print('All three points fall on the same line')
else:
    print('All three points do not fall on the same line')