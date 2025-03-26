import random

def number():
    s=set()
    count=0
    while(len(s)<10):
        val=random.randint(15,45)
        if val in s:
            continue
        else:
            s.add(val)
            
    for j in s.copy():
        if(j<30):
            count+=1
        elif(j>35):
            s.remove(j)
    print("The No of elements less than 30 are:",count)
    print("Updated Set is",s)

number()