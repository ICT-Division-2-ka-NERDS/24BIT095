def freq():
    
    string=input("Enter any string:")
    dic={}
    for i in string:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    print(dic)
    
freq()