print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child ticket is $5.")
        bill = 5
    elif age <= 18:
        print("Youth ticket is $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Middle life crisis ticket")
    else:
        print("Adult ticket $12.")
        bill = 12
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo.upper() == 'Y':
        bill += 3

    print(f"You have to pay ${bill}.")
else:
    print("You stay in the ground")

