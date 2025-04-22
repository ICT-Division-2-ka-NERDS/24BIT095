class Date:
    def __init__(self,date1):
        self.date1=date1
    def __eq__(self,other):
        for i in range(len(self.date1)):
            if self.date1[i]==other.date1[i]:
                continue
            else:
                return False
        return True
    
a=Date([10,7,2025])
b=Date([11,9,2001])
print(a==b) 