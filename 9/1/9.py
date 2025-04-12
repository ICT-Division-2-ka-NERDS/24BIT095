def dict():
    
    def count_alpha_digits(st:str):
        alphabets=list(st)
        numCount=0
        alphaCount=0
        for i in alphabets:
            if i.isnumeric():
                numCount+=1
            elif i.isalpha():
                alphaCount+=1
            else:
                pass
        return {"Digit":numCount,"Alphabets":alphaCount}
    st_count=count_alpha_digits("The Soviet Union was formed in 1922")
    print(st_count)

dict()
