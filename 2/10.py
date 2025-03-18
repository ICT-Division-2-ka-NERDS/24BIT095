A,B = map(int, input('Enter the length and breadth of the rectangle :').split())
Area = A*B
Perimeter = 2*(A+B)
if Area > Perimeter:
    print('The Area of Rectangle is greater than its Perimeter')
elif Area < Perimeter:
    print('The Perimeter of Rectangle is greater than its Area')
else:
    print('The Area and Perimeter of Rectangle are equal')    