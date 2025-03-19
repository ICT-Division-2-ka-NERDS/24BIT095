time = int(input("Enter time in 24-hour format: "))

if time < 12 and time > 0:
    print(time,"AM")
elif time == 12:
    print("Noon")
elif time > 12 and time < 24:
    print(time-12,"PM")
elif time == 24 or time == 0:
    print("Midnight")
else:
    print("Invalid time")
