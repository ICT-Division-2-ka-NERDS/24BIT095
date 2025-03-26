def names():
    
    s=set()
    x=int(input("Enter the no of values you want to add in set:"))
    for i in range(x):
        element=input("Enter the element you want to add in set(starts with A or B only):")
        s.add(element)
        
    a=set()
    b=set()
    for i in s:
        if (i.startswith('a') or i.startswith('A')):
            a.add(i)
        elif (i.startswith('b') or i.startswith('B')):
            b.add(i)
    print(a)
    print(b)
    
names()    
