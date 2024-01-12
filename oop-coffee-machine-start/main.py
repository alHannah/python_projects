from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
process_coffee = CoffeeMaker()
process_money = MoneyMachine()

operating = True
while operating:
    make_order = input(f"What would you like? {menu.get_items()}: ").lower()
    if make_order == "report":
        process_coffee.report()
        process_money.report()
    elif make_order == "off":
        operating = False
    else:
        if menu.find_drink(make_order):
            if process_coffee.is_resource_sufficient(menu.find_drink(make_order)):
                if process_money.make_payment(menu.find_drink(make_order).cost):
                    process_coffee.make_coffee(menu.find_drink(make_order))
