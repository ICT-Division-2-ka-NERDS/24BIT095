class Weather:
    def __init__(self, data):
        self.data = data
    def __contains__(self, item):
        return item in self.data

W = Weather(["Rainfall", "Temperature", "Humidity", "WindSpeed", "Pressure", "Visibility"])
print("Rainfall" in W)  
print("Snowfall" in W)