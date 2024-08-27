from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
power_down = False
coffee_choices = coffee_menu.get_items()


# Get drink choice - check for valid drink name
# Once drink is valid, go to make drink
while not power_down:
    user_selection = input(f"What would you like to drink? ({coffee_choices}): ")
    if user_selection == "off":
        power_down = True
    elif user_selection == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(user_selection)
        print(f"Checking available resources to make your {drink.name}...")
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
