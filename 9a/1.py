def loop():
    
    def fun():
        print("This is fun function")
    def disp():
        print("This is disp function")
    def msg():
        print("This is msg function")
    l=[fun,disp,msg]
    for i in l:
        i()
loop()