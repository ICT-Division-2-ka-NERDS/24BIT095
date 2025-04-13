def palidrome():
    
    lst = ['madam','Python',"malayalam",12321]
    def isPalindrome(s):
        if(type(s)==str):
            if(s[::-1]==s[::]):
                return True
            else:
                return False
        else:
            return False
    l=list(filter(isPalindrome,lst))
    print(l)
    
palidrome()