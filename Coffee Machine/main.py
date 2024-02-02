from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker() 
moneymachine = MoneyMachine()
menu = Menu()

while True:
    order = menu.get_items()
    choice = input(f"What do u want to have {order} ")
    if choice == 'report':
        coffeemaker.report()
        moneymachine.report()
        continue
    if choice == 'off':
        exit()
    drink = menu.find_drink(choice)

    if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
        coffeemaker.make_coffee(drink)


