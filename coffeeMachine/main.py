from coffee_resources_list import MENU, resources


def refill():
    resources['water'] = 300
    resources['milk'] = 300
    resources['coffee'] = 200


def run_report():
    """Print out a report of current resource values"""
    global income
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${income:.2f}")


def check_resources(drink):
    """When the user chooses a drink, the program will check if there are enough resources to make that drink."""
    for item in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return True
        else:
            return False


def get_money():
    print("Please insert your coins.")
    total_inserted = (int(input("How many quarters? "))) * .25
    total_inserted += (int(input("How many dimes? "))) * .10
    total_inserted += (int(input("How many nickles? "))) * .05
    total_inserted += (int(input("How many pennies? "))) * .01
    return total_inserted


def making_coffee(coffee_type):
    """If the transaction is successful and there are enough resources to make the drink the user selected, then
    the ingredients to make the drink will be deducted from the coffee machine resources."""
    cost = MENU[coffee_type]['cost']
    coffee_funded = False
    global income
    if not check_resources(coffee_type):
        while not coffee_funded:
            print(f"The cost is ${cost}. Please insert your coins.")
            user_money = get_money()
            if user_money < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                # If the user has inserted too much money, the machine should offer change.
                if user_money > cost:
                    change = round((user_money - cost), 2)
                    print(f"Here is ${change} dollars in change.")
                    user_money -= change
                print(f"Thank you. Here is your {coffee_type}. Enjoy!")
                for item in MENU[coffee_type]["ingredients"]:
                    resources[item] -= MENU[coffee_type]['ingredients'][item]
                coffee_funded = True
                income += user_money


power_down = False
income = 0
while not power_down:
    user_selection = input("What would you like? (Enter espresso, latte or cappuccino): ").lower()
    # When the user enters “report”, a report should be generated that shows the current resource values.
    if user_selection == 'report':
        run_report()
    elif user_selection == 'refill':
        refill()
    # Turn off the Coffee Machine by entering “off” to the prompt.
    elif user_selection == 'off':
        power_down = True
    else:
        coins_added = making_coffee(user_selection)
