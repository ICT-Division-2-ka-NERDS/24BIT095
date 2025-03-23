import random

def pos():
    
    list=[]
    for i in range(20):
        list.append(random.randint(1,100))
    print(list)
    occ=int(input("Enter the number whose occurence is required between 1-100:"))
    for j in range(10):
        if list[j]==occ:
            print(j)

pos()
