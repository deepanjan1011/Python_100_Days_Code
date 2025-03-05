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
game_img = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if choice >= 0 and choice <= 2:
    print(game_img[choice])
comp_choice = random.randint(0,2)
print(f"Computer chose: ")
print(game_img[comp_choice])
if choice >= 3 and comp_choice < 0:
    print("You typed an invalid number. You lose!")
elif choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice > choice:
    print("You lose!")
elif choice > comp_choice:
    print("You Win!")
elif choice == comp_choice:
    print("It's a draw!")



