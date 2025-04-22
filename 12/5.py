class Time:
    def __init__(self, sec, min, hour):
        self.sec = sec
        self.min = min
        self.hour = hour
        self.convert()
    def convert(self):
        if self.sec > 59:
            self.min += self.sec // 60
            self.sec %= 60
        if self.min > 59:
            self.hour += self.min // 60
            self.min %= 60
        if self.hour > 23:
            self.hour %= 24
    def add(self, other):
        self.sec += other.sec
        self.min += other.min
        self.hour += other.hour
        self.convert()
    def subtract(self, other):
        self.sec -= other.sec
        self.min -= other.min
        self.hour -= other.hour
        if self.sec < 0:
            self.sec += 60
            self.min -= 1
        if self.min < 0:
            self.min += 60
            self.hour -= 1
        if self.hour < 0:
            self.hour += 24
        self.convert()
    def multiply(self, factor):
        total_seconds = (self.hour * 3600 + self.min * 60 + self.sec) * factor
        self.hour = total_seconds // 3600
        self.min = (total_seconds % 3600) // 60
        self.sec = total_seconds % 60
        self.convert()
    def divide(self, factor):
        total_seconds = (self.hour * 3600 + self.min * 60 + self.sec) // factor
        self.hour = total_seconds // 3600
        self.min = (total_seconds % 3600) // 60
        self.sec = total_seconds % 60
        self.convert()
    def display(self):
        print(f"{self.hour:02}:{self.min:02}:{self.sec:02}")



A = Time(10, 23, 54)  
B = Time(6, 18, 12)   

print("Time A:")
A.display()
print("Time B:")
B.display()
A.add(B)
print("Addition:")
A.display()
A.subtract(B)
print("Subtraction:")
A.display()
A.multiply(2)
print("Multiplication with 2:")
A.display()
A.divide(2)
print("Divsion by 2:")
A.display()
 
