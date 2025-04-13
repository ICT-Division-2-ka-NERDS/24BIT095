def numbers():
    
    l1=[1,2,3,4,5,6]
    l2=[6,5,4,3,2,1]
    l=list(map(lambda x,y:x+y,l1,l2))
    print(l)
numbers()