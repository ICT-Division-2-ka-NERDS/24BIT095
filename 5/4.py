import random

def integer():
    list=[]
    for i in range(30):
        list.append(random.randint(-100,100))
    print(list)
    positive=[]
    negative=[]
    for i in list:
        if i>0:
            positive.append(i)
        else:
            negative.append(i)
    print(positive,negative)
    print("The number of positive numbers are:",len(positive))
    print("The number of negative numbers are:",len(negative))
    
integer()
