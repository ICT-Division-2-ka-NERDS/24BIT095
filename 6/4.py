food_prices = [("Aloo Tikki", 120), ("Pizza", 250), ("Frankie", 180), ("Hakka Noodles", 100), ("CBM", 150)]

def get_price(item):
    return item[1]

sorted_food_prices = sorted(food_prices, key=get_price, reverse=True)

print(sorted_food_prices)
