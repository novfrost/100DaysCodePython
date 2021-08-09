# Import required libraries
from data import *

# Global variables
continue_serving = True
money = 0.0
payment = 0.0


def get_recipe(coffee_type):
    return MENU[coffee_type]['ingredients']


def enough_ingredients(coffee):
    can_make_coffee = True
    for k, v in coffee.items():
        if resources[k] < coffee[k]:
            print(f"Sorry there is not enough {k}.")
            can_make_coffee = False
    return can_make_coffee


def make_coffee(list_of_ingredients):
    for k, v in list_of_ingredients.items():
        resources[k] -= list_of_ingredients[k]


# TODO: 1) Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while continue_serving:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 2) Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice.lower() == "off":
        continue_serving = False
    # TODO 3) Print report
    elif user_choice.lower() == 'report':
        for key, value in resources.items():
            print(f"{key.capitalize()}: {value}ml")
        print(f"Money: ${money}")
    else:
        # TODO 4)  Check resources sufficient?
        coffee_requested = get_recipe(user_choice)

        if enough_ingredients(coffee_requested):

            # TODO 5) Process coins.
            payment += float(input("How many quarters: ")) * .25
            payment += float(input("How many dimes: ")) * .1
            payment += float(input("How many nickles: ")) * .05
            payment += float(input("How many pennies: ")) * 0.01

            coffee_cost = MENU[user_choice]['cost']

            # TODO 6) Check transaction successful?
            if payment <= coffee_cost:
                print("Sorry that's not enough money. Money refunded.")
                payment = 0
            else:
                money += coffee_cost
                if payment > coffee_cost:
                    user_change = round((payment - coffee_cost), 2)
                    print(f"Here is ${user_change} dollars in change.")
                payment = 0

                # TODO 7) Make Coffee.
                make_coffee(coffee_requested)
                print(f"Here is your {user_choice}. Enjoy!")