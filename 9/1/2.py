def function():
    def compute(n:int):
        ans=0
        for i in range(1,5):
            ans=ans+int(str(n)*i)
        return ans
    for j in range(4,8):
        print(compute(j))
function()