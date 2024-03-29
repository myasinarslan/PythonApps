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

#Write your code below this line 👇
import random

list = [rock, paper, scissors]

def game ():
  x = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors."))
  
  user_choice = list[x]
  print(f'Your choice: {user_choice}')
  
  AI = random.randint(0,2)
  if x >= 0 and x <=2:
    print(f'Computer choice: {list[AI]}')
  
  
  if x == AI:
    print('Draw')
  
  if x == 0 and AI == 1:
    print('You lose')
  
  if x == 1 and AI == 0:
    print('You win')
  
  if x == 1 and AI == 2:
    print('You lose')
  
  if x == 2 and AI == 1:
    print('You win')
  
  if x == 2 and AI == 0:
    print('You lose')
  
  if x == 0 and AI == 2:
    print('You win')

result = 'yes'
while result == 'yes':
  game()
  result = (input("Do you want to play again? Type 'Yes' or 'No'")).lower()

print("Thank you for playing Yasin's RPS!")
  
  