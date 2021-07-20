# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
test_name = name1.lower() + name2.lower()
letter_t = test_name.count('t')
letter_r = test_name.count('r')
letter_u = test_name.count('u')
letter_e = test_name.count('e')

total_true = letter_t + letter_r + letter_u + letter_e

letter_l = test_name.count('t')
letter_o = test_name.count('r')
letter_v = test_name.count('u')
letter_e = test_name.count('e')

total_love = letter_l + letter_o + letter_v + letter_e

score = int(str(total_true) + str(total_love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


