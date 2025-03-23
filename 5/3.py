import random

def duplicates():
    list=[]
    for i in range(50):
        list.append(random.randint(1,30))
    print(list)
    l=[]
    for i in list:
        if i not in l:
            l.append(i)
    print(l)

    print("The number of duplicates is:",len(list)-len(l))
    
duplicates()