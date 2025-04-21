def merge_lines():
    f1 = open("C:\\Users\\admin\\Desktop\\Idiotic stuff (2nd sem)\\Python Assignments\\10\\f1.txt", "r")
    f2 = open("C:\\Users\\admin\\Desktop\\Idiotic stuff (2nd sem)\\Python Assignments\\10\\f2.txt", "r")
    f3 = open("merged.txt", "w+")

    a = f1.readlines()
    b = f2.readlines()

    for i in range(max(len(a), len(b))):
        if i < len(a):
            f3.write(a[i])
        if i < len(b):
            f3.write(b[i])

    f1.close()
    f2.close()
    f3.close()

merge_lines()