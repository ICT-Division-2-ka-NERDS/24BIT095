def alphabet():
    
    def isPangram(s:str):
        set1=set(s.lower())
        alphast='abcdefghijklmnopqrstuvwxyz'
        alphaset=set(alphast)
        for s in alphaset:
            if set(s) <= set1:
                continue
            
    ans1=isPangram("The quick brown fox jumps over the lazy dog")
    ans2=isPangram("Crazy Fredrick bought many very exquisite opal jewels")
    print(ans1)
    print(ans2)
    
alphabet()