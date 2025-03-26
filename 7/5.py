def grocery():
    
    d_price={"KitKat":120,"Mogu-Mogu":20,"Rice":120}
    d_quantity={"KitKat":1,"Mogu-Mogu":2,"Rice":10}
    total=0
    for key in d_price.keys():
        total=total+d_price[key]*d_quantity[key]
    print(total)
    
grocery()