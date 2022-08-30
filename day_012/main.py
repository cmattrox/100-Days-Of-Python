import random
import sys

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose your difficulty: 'easy' or 'hard': ").lower()

if (difficulty == "easy"):
    guesses = 10
elif (difficulty == "hard"):
    guesses = 5

number = random.randint(1, 100)

while guesses > 0:
    print(f"You have {guesses} guesses left.")
    guess = int(input("Guess a number: "))

    if (guess == number):
        print(f"You are correct! The number was {number}")
        sys.exit()
    elif (guess > number):
        print("Too high.")
        guesses -= 1
    elif (guess < number):
        print("Too low")
        guesses -= 1

print(f"You ran out of guesses. The number was {number}")