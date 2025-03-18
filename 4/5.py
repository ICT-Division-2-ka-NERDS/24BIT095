def q5():
    for a in range(1, 31):
        for b in range(a, 31):
            for c in range(b, 31):
                if a * a + b * b == c * c:
                    print(a, b, c)
q5()
