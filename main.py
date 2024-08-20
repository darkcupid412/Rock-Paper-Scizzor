import random

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

rps_list = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

user_choice = rps_list[user_input]
comp_choice = random.choice(rps_list)

print(f"\nYou chose:\n{user_choice}\nComputer chose:\n{comp_choice}")

if (user_choice == rock and comp_choice == scissors) or \
   (user_choice == scissors and comp_choice == paper) or \
   (user_choice == paper and comp_choice == rock):
    print("You win!")
elif user_choice == comp_choice:
    print("It's a tie!")
elif (user_choice == rock and comp_choice == paper) or \
     (user_choice == scissors and comp_choice == rock) or \
     (user_choice == paper and comp_choice == scissors):
    print("You lost.")
else:
    print("Invalid Input. Please try again")
