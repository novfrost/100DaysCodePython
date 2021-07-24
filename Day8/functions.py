# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(name):
    print(f"Primera accion {name}")
    print("Segunda accion")
    print("Tercera accion")


def greet_with_name(name="No name"):
    print(f"Hello {name}")

# Functions with more than one imput
def greet_with(name,location):
    print(f"Hello {name}, what is it like in {location}")

greet_with("Carlos","Madrid")
greet_with(location="Madrid",name="Carlos")
