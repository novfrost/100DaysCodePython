rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

ops = [rock,paper,scissors]
user_selcted = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_selcted >= 3:
    print("Invalid number, you lose")
else:
    computer_select = random.randint(0,2)

    print(ops[user_selcted])
    print("Computer chose:")
    print(ops[computer_select])
        
    if user_selcted == computer_select:
        print("Its a tie")
    elif user_selcted == 0 and computer_select == 1:
        print("You lose")
    elif user_selcted == 1 and computer_select == 2:
        print("You lose")
    elif user_selcted == 2 and computer_select == 0:
        print("You lose")
    else:
        print("You win!")