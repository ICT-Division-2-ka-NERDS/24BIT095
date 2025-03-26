def names():
    
    s = {input("Enter a name: ") for i in range(5)}

    old_name = input("Enter the name to modify: ")
    if old_name in s:
        s.remove(old_name)
        s.add(input("Enter the modified name: "))
    else:
        print("Value not found in set")

    for i in range(2):
        name = input("Enter a name to delete: ")
        s.discard(name)  

    print(s)

names()
