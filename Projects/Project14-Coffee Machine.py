menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
   "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.1
    total += int(input("How many Nickles?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.01
    return total

def transaction(money_received, drink_cost):
    """RETURN TRUE WHEN THE PAYMENT IS ACCEPTED OR FALSE IF MONEY IS INSUFFICIENT"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money is refunded")
        return False

def coffee(name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {name}, Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if choice == "off":
        is_on = False 
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print("Money: ${profit}")
    else:
        drink = menu[choice]
        if resource(drink["ingredients"]):
            pay = coins()
            if transaction(pay, drink["cost"]):
                coffee(choice, drink["ingredients"])
