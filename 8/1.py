def uppercase():
    
    words=[]
    s=set()
    x=int(input("Enter the number of words you want to enter in list:"))
    for i in range(x):
        word=input("Enter the word:")
        words.append(word.upper())
    s=set(words)
    print(s)

uppercase()