A = int(input('Enter A year :'))
if A % 4 == 0 and A % 100 != 0 or A % 400 == 0:
    print('This is A leap year')
else:
    print('This is not A leap year')