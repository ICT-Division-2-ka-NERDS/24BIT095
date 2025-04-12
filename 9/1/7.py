def word():
    
    def ispalindrome(st:str):
        st=st.lower()
        st=st.replace(" ","")
        for i in range(len(st)//2):
            if i==" ":
                continue
            else:
                if(st[i]==st[-(i+1)]):
                    pass
                else:
                    return False
        return True
    st=input("Enter the string you want to check:")
    print("The string {st}",ispalindrome(st))
    
word()