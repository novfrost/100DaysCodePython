print("Welcome to the tip calculator.")

# Get the amount for the bill
total = float(input("What was the total bill? $"))

# Calculate the total with the tip percentage
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_tip = total * (1+(tip/100))

# Get the amount of people
people = int(input("How many people to split the bill? "))

# Calculate with rounded to two decimals
pay_total = "{:.2f}".format(total_tip / people)

# Print the amount
message = f"Each person should pay: ${pay_total}"
print(message)