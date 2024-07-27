MENU = {
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


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def processing_ingredients(customer_order):
    if customer_order == "espresso":
        resources["water"] = resources["water"] - MENU[customer_order]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[customer_order]["ingredients"]["coffee"]
    else:
        resources["water"] = resources["water"] - MENU[customer_order]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[customer_order]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[customer_order]["ingredients"]["coffee"]


def processing_payment(quarters, dimes, nickels, pennies, customer_order):
    quarters = 0.25 * quarters
    dimes = 0.10 * dimes
    nickels = 0.05 * nickels
    pennies = 0.01 * pennies
    total_pay = quarters + dimes + nickels + pennies
    order_cost = MENU[customer_order]["cost"]
    change = total_pay - order_cost
    rounded_change = round(change, 2)
    # TODO 2.2 Check if enough money "Sorry that's not enough money. Money refunded."
    if change <= 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        # TODO 3. Give Change and Coffee "Here is {} in change." "Here is your {} ☕️. Enjoy!"
        print(f"Here is ${rounded_change} in change. Here is your {customer_order} ☕️. Enjoy!")


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


money = 0
operating = True
while operating:
    # TODO 1. Ask for Order
    make_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if make_order == "report":
        report()
    # TODO 4. Ask for another order Turn off by saying "off" "report" to show resource
    elif make_order == "off":
        operating = False
    elif make_order in MENU:
        processing_ingredients(make_order)
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        if water <= 0:
            print(f"Sorry there is not enough Water.")
            operating = False
        elif milk <= 0:
            print(f"Sorry there is not enough Milk.")
            operating = False
        elif coffee <= 0:
            print(f"Sorry there is not enough Coffee.")
            operating = False
        else:
            # TODO 2. Insert coins penny = 0.01, nickel = 0.05, dime = 0.10, quarter = 0.25
            print("Please insert coins.")
            customer_quarters = int(input("how many quarters?: "))
            customer_dimes = int(input("how many dimes?: "))
            customer_nickels = int(input("how many nickels?: "))
            customer_pennies = int(input("how many pennies?: "))

            processing_payment(customer_quarters, customer_dimes, customer_nickels, customer_pennies, make_order)
            charge = MENU[make_order]["cost"]
            money += charge


