from art import *

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculation():
    print(logo)

    user_input = 'y'
    num1 = float(input("What is the first number?: "))

    for key in operations:
        print(key)

    while user_input != 'n':

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number?: "))

        calculation_funcion = operations[operation_symbol]
        first_result = calculation_funcion(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {first_result}")

        user_input = input(f"Type 'y' to continue calculating with {first_result}, or type 'n' to start a new calculation: ")

        if user_input == 'y':
            num1 = first_result
        else:
            calculation()

calculation()

# operation_symbol = input("Pick another operation: ")
# num3 = int(input("What is the next number?: "))
# calculation_funcion = operations[operation_symbol]
# second_result = calculation_funcion(first_result, num3)

# print(f"{first_result} {operation_symbol} {num3} = {second_result}")