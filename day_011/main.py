import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game = True
os.system('clear')

def deal_card():
    return random.choice(cards)

def compare(user, computer):
    if (user == computer):
        print("Draw!")
    elif (computer == 0):
        print("Opponent has blackjack. You lose.")
    elif (user == 0):
        print("You have a blackjack. You win!")
    elif (user > 21):
        print("You went over. You lose.")
    elif (computer > 21):
        print("Opponent went over. You win!")
    elif (computer > user):
        print("You lose.")
    elif (user > computer):
        print("You win!")

def calculate_score(list):
    score = sum(list)

    if (len(list) == 2 and score == 21):
        return 0
    elif (len(list) == 2 and score > 21):
        list.remove(11)
        list.append(1)

    return score

while game:
    user_cards = []
    computer_cards = []
    over = True
    user_input = 'y'

    print(logo)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your hand: {user_cards} Score: {user_score}")
    print(f"Opponent's first card: {computer_cards[0]}")

    if (user_score == 0 or computer_score == 0 or user_score > 21):
        user_input = 'n'

    while user_input == 'y':
        user_input = input("Type 'y' to draw another card or 'n' to pass: ").lower()
        if (user_input == 'y'):
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)

            if (user_score > 21):
                user_input = 'n'
            else:
                print(f"Your hand {user_cards} Score: {user_score}")

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your hand: {user_cards} Final score: {user_score}")
    print(f"Opponent's hand: {computer_cards} Final score: {computer_score}")
    compare(user_score, computer_score)
    
    cont = input("Press 'y' if you want to play blackjack or 'n' if you don't: ").lower()

    if (cont == "n"):
        game = False
    else:
        os.system("clear")