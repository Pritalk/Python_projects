'''
Build a Rock, Paper, Scissors game.
Take input from user, and use random module to take 2nd input and mention it as computer's input.
Play and enjoy the game:)
'''


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
lst = [rock, paper, scissors]
print(lst)
player1 = int(input("Please choose 0 for 'rock', 1 for 'paper' and 2 for 'scissor'\n"))
print(f" Your response: {lst[player1]}")
player2 = random.randint(0, 2)
print(player2)
print(f"computer's response: {lst[player2]}")

if player1 == player2:
    print("It's a tie")
elif player1 == 1 and player2 == 0:
    print("You win")
elif player1 == 2 and player2 == 1:
    print("You win")
elif player1 == 3 and player2 == 2:
    print("You win")
else:
    print("You lose")
