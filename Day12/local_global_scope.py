################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# There is no block scopre
# if, while, for, dont have local scope

# Modifying Global Scope

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(enemies)

increase_enemies()
print(enemies)

# Global Constants

PI = 3.14159