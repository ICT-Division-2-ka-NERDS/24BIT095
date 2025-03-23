def list_comprehension():

    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [4, 5, 6, 7, 8, 9]

    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)

    print(list3)

list_comprehension()