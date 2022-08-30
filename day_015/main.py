import sys

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
    "money": 0
}

def prompt():
    choice = input("What would you like? (espresso / latte / cappuccino): ").lower()
    return choice

def turnOff ():
    sys.exit()

def printReport():
    for key, val in resources.items():
        if (key == "water" or key == "milk"):
            print(f"{key}: {val}ml")
        elif (key == "coffee"):
            print(f"{key}: {val}g")
        elif (key == "money"):
            print(f"{key}: ${val}")

def checkResources(choice):
    ing = choice['ingredients']
    for key, val in ing.items():
        if (resources[key] < val):
            return key
        
    return True

def processCoins(q, d, n, p):
    return ((q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01))

def checkPrice(money, choice):
    if (money < choice['cost']):
        print("Sorry that's not enough money. Money refunded.")
    else:
        resources['money'] += choice['cost']
        return money - choice['cost']

def makeCoffee(choice):
    for key, val in choice['ingredients'].items():
        resources[key] -= val

    print("Here is your drink. Enjoy!")

choice = prompt()

while choice != "off":
    if (choice == ""):
        choice = prompt()
    elif (choice == "report"):
        printReport()
        choice = ""
    else:
        res = checkResources(MENU[choice])

        if (res == True):
            print("Please insert coins.")
            q = int(input("How many quarters?: "))
            d = int(input("How many dimes?: "))
            n = int(input("How many nickels?: "))
            p = int(input("How many pennies?: "))

            total = processCoins(q, d, n, p)

            change = checkPrice(total, MENU[choice])

            if (change > -1):
                print(f"Here is ${round(change, 2)} in change.")

                makeCoffee(MENU[choice])
                choice = ""
        else:
            print(f"Sorry there is not enough {res}")
            choice = ""
    
