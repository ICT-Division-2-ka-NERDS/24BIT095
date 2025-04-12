def intersection():
    
    def create_list(l1:list,l2:list):
        l=[]
        for i in l1:
            if(i in l2):
                l.append(i)
            else:
                continue
        return l
    lst=create_list([1,4,2,3,0,8,76,5,6,7],[7,3,4,5,4,5,6,7,4,3,4,56,45,3,2])
    print(lst)
    
intersection()