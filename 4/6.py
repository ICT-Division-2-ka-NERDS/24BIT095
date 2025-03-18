for hour in range(24):
    if hour == 0:
        print("12:00 AM") 
    elif hour == 12:
        print("12:00 PM")  
    elif hour < 12:
        print(str(hour) + ":00 AM")
    else:
        print(str(hour - 12) + ":00 PM")
