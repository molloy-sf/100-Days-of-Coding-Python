# Coffee Machine

This Python project implements a simple coffee machine that allows users to select and purchase beverages. The program manages resources, processes transactions, and provides a report of current resource levels.

## Features

- Choose from three types of coffee: Espresso, Latte, and Cappuccino.
- Check available resources (water, milk, coffee) and the total income.
- Refill resources as needed.
- Handle monetary transactions, including change if too much is inserted.

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the code files.
2. Ensure you have the following files:
   - `coffee_machine.py` (the main script for the coffee machine)
   - `coffee_resources_list.py` (contains the `MENU` and `resources` data)

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the coffee machine script.
3. Run the script:

   ```bash
   python coffee_machine.py

    Follow the prompts to select a drink, check resources, refill, or turn off the machine.

Menu and Resources

The coffee_resources_list.py file includes:
MENU

Defines the available drinks with their ingredients and costs:

    Espresso
        Ingredients: 50ml water, 0ml milk, 18g coffee
        Cost: $1.50

    Latte
        Ingredients: 200ml water, 150ml milk, 24g coffee
        Cost: $2.50

    Cappuccino
        Ingredients: 250ml water, 100ml milk, 24g coffee
        Cost: $3.00

Resources

Initial resources available in the coffee machine:

python

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

Functions

    refill(): Refills the resources to preset values (300ml water, 300ml milk, 200g coffee).
    run_report(): Displays the current resource levels and total income.
    check_resources(drink): Checks if there are enough resources to make the selected drink.
    get_money(): Prompts the user to insert coins and returns the total amount inserted.
    making_coffee(coffee_type): Processes the transaction and deducts the necessary resources if the transaction is successful.

Example Interaction

mathematica

What would you like? (Enter espresso, latte or cappuccino): latte
Please insert your coins.
How many quarters? 2
How many dimes? 1
How many nickles? 0
How many pennies? 4
Thank you. Here is your latte. Enjoy!

Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and create a pull request.
License

This project is open-source and available under the MIT License.

