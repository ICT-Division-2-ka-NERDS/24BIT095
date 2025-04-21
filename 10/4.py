def copyupper():
    
    f1 = open("C:\\Users\\admin\\Desktop\\Idiotic stuff (2nd sem)\\Python Assignments\\10\\4.txt", "r+")
    f2 = open("4.txt", "w+")
    for line in f1:
        f2.write(line.upper())
    f1.close()
    f2.close()

copyupper()