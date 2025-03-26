def is_leap_year(year):
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_months[1] = 29 
    return days_in_months[month - 1]

def total_days(d, m, y):
    days = 0
    
    for year in range(1, y):
        days += 366 if is_leap_year(year) else 365
    
    for month in range(1, m):
        days += days_in_month(month, y)
    
    days += d
    
    return days

def days_between_dates(date1, date2):

    total_days1 = total_days(date1[0], date1[1], date1[2])
    total_days2 = total_days(date2[0], date2[1], date2[2])
    
    
    return abs(total_days2 - total_days1)

date1 = (10, 7, 2006)  
date2 = (15, 4, 2025)  
print("Number of days between the two dates:", days_between_dates(date1, date2))
