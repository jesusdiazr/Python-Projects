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

earnings = 0


def start_machine():
    coffee = (input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if coffee == "report":
        for key in resources:
            if key == "coffee":
                unit = "gr"
            else:
                unit = "ml"
            print(f"{key.capitalize()}: {resources[key]}{unit}")
        print(f"Money: ${format(earnings, '.2f')}\n")
        start_machine()

    elif coffee == "off":
        return

    else:
        if check_stock(coffee):
            print("\n")
            start_machine()
        if take_money(coffee):
            start_machine()
        print(f"Here is your {coffee} ☕. Enjoy!\n")
        start_machine()


def check_stock(coffee):
    if coffee == "espresso":
        if resources["water"] < MENU[coffee]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return 1

        elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return 1

        else:
            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]

    else:
        if resources["water"] < MENU[coffee]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return 1

        elif resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            return 1

        elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return 1

        else:
            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    return 0


def take_money(coffee):
    print("Please insert coins.")
    money = 0
    money += int(input("How many quarters?: ")) * 0.25
    money += int(input("How many dimes?: ")) * 0.10
    money += int(input("How many nickles?: ")) * 0.05
    money += int(input("How many pennies?: ")) * 0.01
    if money < MENU[coffee]["cost"]:
        print("Sorry, that's not enough money. Money refunded.\n")
        return 1
    elif money > MENU[coffee]["cost"]:
        print(f"Here is ${format(money - MENU[coffee]['cost'], '.2f')}  in change.")
    global earnings
    earnings += MENU[coffee]["cost"]
    return 0


start_machine()
