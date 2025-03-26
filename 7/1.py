def dict():
    
    d={}
    d0={"Brand": "Porsche","Model": "911","Color": "Black","Year": 2020}
    d1={'Type' : 'Fruit', 'Name' : 'Apple', 'Color' : 'Red'}
    d2={"Germany": "Berlin", "Italy": "Rome", "Japan": "Tokyo"}
    d.update(d0)
    d.update(d1)
    d.update(d2)
    print(d)
    
dict()
    