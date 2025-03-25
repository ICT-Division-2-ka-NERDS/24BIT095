def name():
    
    lst = [('Dhyey'), ('Prem', 'Arpit'), 'Yesha', 'Anoushka', 'Jay', ('Shaival'), ('Selvi')]
    boys = 0
    girls = 0

    for i in lst:
        if isinstance(i, tuple):  
            boys += len(i)  
        else:
            girls += 1  

    print('The number of Girls is:', girls)
    print('The number of Boys is:', boys)


def main():
    name()


main()