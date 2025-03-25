def remove():
    
    list=[(),'Dhyey',('lst',),[1,2,3],[]]
    for i in list:
        if(type(i)==tuple and len(i)==0):
            list.remove(i)
        else:
            pass
    print(list)
    
remove()    