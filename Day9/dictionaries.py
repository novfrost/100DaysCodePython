programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop":"The action of doing something over and over again"}

# Retrieve items from a Dictionary
#print(programming_dictionary["Bug"])

# Addin new items to the dictionary
programming_dictionary["Typo"] = "An error from the keyboard that doest not comppile"
#print(programming_dictionary)

# Wipe an existing dictionary
#programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "This is an instect"
#print(programming_dictionary)

# Loop trough a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary
# travel_log = {
#     "France": ["Paris","Lille","Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 20
    }
}

#print(travel_log["France"]["cities_visited"])


# Nesting dictionary in a list
travel = [
    {
        "country":"France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 20
    }
]

print(travel[0]["total_visits"])