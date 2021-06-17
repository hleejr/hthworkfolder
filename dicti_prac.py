'''

'''
# The _ of _ is _ (The grocery price of chicken is 1.59)

grocery_price = {
    "Chicken": 1.59,
    "Beef": 1.99,
    "Cheese": 1,
    "Milk": 2.5,
}

NBA_jersey_numbers = {
    "Lebron James": 23, 
    "Kevin Durant": 35, 
    "Stephen Curry": 30, 
    "Damian Lillard": 0,
}

stock_number = {
    "Jordan 13": 1,
    "Yeezy": 8,
    "Foamposite": 10,
    "Air Max": 5,
    "SB Dunk": 20
}

stock_number["SB Dunk"] -= 2
stock_number["Yeezy"] += 1
stock_number["SB Dunk"] += 7
stock_number["Jordan 13"] += 7
stock_number["Yeezy"] += 7
stock_number["Foamposite"] += 7
stock_number["Air Max"] += 7
stock_number["SB Dunk"] += 7
stock_number["Jordan 13"] -= 3
stock_number["Yeezy"] -= 3
stock_number["Foamposite"] -= 3
stock_number["Air Max"] -= 3
stock_number["SB Dunk"] -= 3

NBA_jersey_numbers["Donovan Mitchell"] = 45
del NBA_jersey_numbers["Kevin Durant"]

chicken_price = grocery_price["Chicken"]
# print(chicken_price)

steph_jersey = NBA_jersey_numbers["Stephen Curry"]
# print(steph_jersey)

NBA_jersey_numbers["Lebron James"] -= 17
# print(NBA_jersey_numbers)
print(stock_number)

def total_price( item1, item2 ):
    price1 = grocery_price[item1]
    price2 = grocery_price[item2]
    total = price1 + price2

    return total

def price_difference( item1, item2 ):
    price1 = grocery_price[item1]
    price2 = grocery_price[item2]
    price_difference = abs(price1 - price2)

    return price_difference

def restock( shoe_name, num ):
    old_stock = stock_number[shoe_name]
    stock_number[shoe_name] = old_stock * num

    return stock_number

def clearance_sale( shoe_name, num ):
    old_stock = stock_number[shoe_name]
    stock_number[shoe_name] = old_stock // num

    return stock_number

print( clearance_sale( "SB Dunk", 5 ) )