'''
Chicken $1.59
Beef $1.99
Cheese $1.00
Milk $2.50

Next is updating existing values in a dictionary. To update the value for a given key we use the same bracket notation approach and variable reassignment. We can either replace the value entirely or modify it using arithmetic operators. Using the same NBA_players dictionary as an example, what if I wanted to change Lebron’s jersey number to 6, which was his number during his time in Miami? 

Jordan 13,  1
Yeezy, 8
Foamposite, 10
Air Max, 5
SB Dunk, 20

Update your new dictionary and its stored values based on the prompts below and print your results:
- A customer came in to purchase 2 pairs of  SB Dunks
- A customer came in to return a pair of Yeezys
- The store got a new shipment. All stock increases by 7.
- There is a special sale at the store. All stock decreases by 3.

git commit commands:

1. git push * 
2. git commit -m "adding dictionary practice file"
3. git push



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
print(chicken_price)

steph_jersey = NBA_jersey_numbers["Stephen Curry"]
print(steph_jersey)

NBA_jersey_numbers["Lebron James"] -= 17
print(NBA_jersey_numbers)