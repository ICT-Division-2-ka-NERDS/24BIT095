def temprature():

    fahrenheit = [510, 212, 420, 69, 451] 
    celsius = []

    for i in fahrenheit:
        celsius.append((i - 32) * 5 // 9)

    print(celsius)

temprature()