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

options = [rock, paper, scissors]

user = input("Enter 0 for rock, 1 for paper, or 2 for scissors: ")

computer = random.randint(0,2)

user = int(user)

print("You chose:")
if user > 2 or user < 0:
    print("You must choose a number between 0 and 2.")
else :
    print(options[user])

print("The computer chose:")
print(options[computer])

if (user == 0 and computer == 0):
    print("Draw")
elif (user == 1 and computer == 1):
    print("Draw")
elif (user == 2 and computer == 2):
    print("Draw")
elif (user == 0 and computer == 2):
    print("You win!")
elif (user == 1 and computer == 0):
    print("You win!")
elif (user == 2 and computer == 1):
    print("You win!")
elif (user == 2 and computer == 0):
    print("Computer won")
elif (user == 1 and computer == 2):
    print("Computer won")
elif (user == 0 and computer == 1):
    print("Computer won")
else: 
    print("You must choose a number between 0 and 2")