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


# res=resources


paisa=0
while True:
    order = input("What would you like: (espresso, cappuccino, latte): ")
    if order == "report":
        for key in resources:
            print(f"{key}:{resources[key]}")
        print("money:",paisa)
        continue


    def suff():
        for item in resources:
            if order == "espresso" and item == "milk":
                continue
            elif resources[item] < MENU[order]["ingredients"][item]:
                print(f"Sorry there's not enough {item}")
                return False
        return True


    if suff()==True:
        if order == "espresso" or "latte" or "capuccino":
            print("Please insert coins.")
            a = float(input("how many quarters?: "))
            b = float(input("how many dimes?: "))
            c = float(input("how many nickles?: "))
            d = float(input("how many pennies?: "))
            # rem_resources = resources["water"]-MENU[order]["ingredients"]["water"]
            money = a*0.25+b*0.1+c*0.05+d*0.01
            # remr = resources
            if money >= MENU[order]["cost"]:
                change = (a*0.25+b*0.1+c*0.05+d*0.01) - MENU[order]["cost"]
                print(f"Here's ${round(change, 2)} in change.")
                print(f"Here's your {order}☕. Enjoy! ")
                resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
                if order != "espresso":
                    resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
                paisa += MENU[order]["cost"]
            elif money < MENU[order]["cost"]:
                print("Sorry, that's not enough money, Money refunded.")
    else:
        print("resources insufficient")




