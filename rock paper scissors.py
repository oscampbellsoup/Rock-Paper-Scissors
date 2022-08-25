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
game_pictures = [rock, paper, scissors]
your_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
your_choice = int(your_choice)
if your_choice == 0:
    print(game_pictures[0])
elif your_choice == 1:
    print(game_pictures[1])
elif your_choice == 2:
    print(game_pictures[2])
else:
    print('Please retype your choice.')
    quit()

print('Computer chose:')
import random
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(game_pictures[0])
elif computer_choice == 1:
    print(game_pictures[1])
elif computer_choice == 2:
    print(game_pictures[2])
    
if your_choice == 0 and computer_choice == 0:
    print('You draw')
if your_choice == 0 and computer_choice == 1:
    print('You lose')
if your_choice == 0 and computer_choice == 2:
    print('You win')
if your_choice == 1 and computer_choice == 0:
    print('You win')
if your_choice == 1 and computer_choice == 1:
    print('You draw')
if your_choice == 1 and computer_choice == 2:
    print('You lose')
if your_choice == 2 and computer_choice == 0:
    print('You lose')
if your_choice == 2 and computer_choice == 1:
    print('You win')
if your_choice == 2 and computer_choice == 2:
    print('You draw')