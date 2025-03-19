def q10():
    n = int(input("Enter the value of n: "))
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

q10()