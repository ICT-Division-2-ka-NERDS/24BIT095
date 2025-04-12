def intersection():
    
    def frequency(st:str):
        st=st.split()
        count={}
        for i in st:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        count=sorted(count.items())
        return count
    c=frequency("Write a function create_list() that creates and returns a list which is an intersection of two lists passed to it".lower())
    print(c)
    
intersection()