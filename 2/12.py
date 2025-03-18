import math
A,B = map(int,input('Enter the Coordinates of the center of the circle:').split())
R = int(input('Enter the radius of the circle:'))
PC = math.sqrt(A**2 + B**2)
if PC < R:
    print('The point is inside the circle')
elif PC == R:
    print('The point is on the circle')  
else:
    print('The point is outside the circle')