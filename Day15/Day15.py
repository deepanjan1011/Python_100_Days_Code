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

is_on = True
mon = 0
while is_on:
    def choice():
        global mon
        global is_on
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "off":
            is_on = False
        else:
            if user_choice == "report":
                print(f"Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${mon}")
            if user_choice == "espresso":

                if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                    print("Sorry there is not enough water!")
                elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                    print("Sorry there is not enough coffee!")
                else:
                    print("Please insert coins.")
                    money()
                    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["espresso"]["cost"]
                mon += MENU["espresso"]["cost"]

            elif user_choice == "latte":

                if resources["water"] <= MENU["latte"]["ingredients"]["water"]:
                    print("Sorry there is not enough water!")
                elif resources["milk"] <= MENU["latte"]["ingredients"]["milk"]:
                    print("Sorry there is not enough milk!")
                elif resources["coffee"] <= MENU["latte"]["ingredients"]["coffee"]:
                    print("Sorry there is not enough coffee!")
                else:
                    print("Please insert coins.")
                    money()
                    resources["water"] -= MENU["latte"]["ingredients"]["water"]
                    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                    mon += MENU["latte"]["cost"]

            elif user_choice == "cappuccino":

                if resources["water"] <= MENU["cappuccino"]["ingredients"]["water"]:
                    print("Sorry there is not enough water!")
                elif resources["milk"] <= MENU["cappuccino"]["ingredients"]["milk"]:
                    print("Sorry there is not enough milk!")
                elif resources["coffee"] <= MENU["cappuccino"]["ingredients"]["coffee"]:
                    print("Sorry there is not enough coffee!")
                else:
                    print("Please insert coins.")
                    money()
                    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    mon += MENU["cappuccino"]["cost"]

    def money():
        quat = float(input("How many quarters?: "))
        dim = float(input("How many dimes?: "))
        nick = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        calc = (quat * 0.25) + (dim * 0.10) + (nick * 0.05) + (pennies * 0.01)
        if calc < MENU["espresso"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        elif calc < MENU["latte"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        elif calc < MENU["cappuccino"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Here is ${calc:.2f} in change.")
            print("Here is your latte 🍵 Enjoy!")

    choice()