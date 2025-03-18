def Grade(marks):
        if 40 <= marks <= 44:
            return 'P Grade'
        elif 45 <= marks <= 49:
            return 'C Grade'
        elif 50 <= marks <= 54:
            return 'B Grade'
        elif 55 <= marks <= 59:
            return 'B+ Grade'
        elif 60 <= marks <= 69:
            return 'A Grade'
        elif 70 <= marks <= 79:
            return 'A+ Grade'
        elif 80 <= marks <= 100:
            return 'O Grade'
        else:
            return 'Fail'

A, B, C = map(int, input('Enter Marks of three subjects: ').split())
if A >= 40 and B >= 40 and C >= 40:
    print('Student has passed')
else:
    print('Student has failed')
        
print('The Average of the three subjects is :', (A+B+C)/3)
print('The Total of the three subjects is :', A+B+C)
print('The Grade of Subject A is :',Grade(A))
print('The Grade of Subject B is :',Grade(B)) 
print('The Grade of Subject C is :',Grade(C)) 