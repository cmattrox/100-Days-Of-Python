import sys, os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

CoffeeMaker.__init__(CoffeeMaker)
MoneyMachine.__init__(MoneyMachine)
Menu.__init__(Menu)

choice = input(f"What would you like? {Menu.get_items(Menu)}: ").lower()

while choice != "off":
    if (choice == ""):
        choice = input(f"What would you like? {Menu.get_items(Menu)}: ").lower()
    elif (choice == "report"):
        CoffeeMaker.report(CoffeeMaker)
        MoneyMachine.report(MoneyMachine)
        choice = ""
    else:
        drink = Menu.find_drink(Menu, choice)
        if (CoffeeMaker.is_resource_sufficient(CoffeeMaker, drink)):
            if (MoneyMachine.make_payment(MoneyMachine, drink.cost)):
                CoffeeMaker.make_coffee(CoffeeMaker, drink)
                choice = ""
            else:
                choice = ""
        else:
            choice = ""
        