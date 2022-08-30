import random
from words import word_list
from ascii_art import stages, logo

print(logo)
chosen_word = random.choice(word_list)
display = []

for letter in chosen_word:
    display.append("_")
game_over = False
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    for idx, letter in enumerate(chosen_word):
        if letter == guess:
            display[idx] = guess
    
    if guess not in chosen_word:
        lives -= 1
        
    print(display)
    print(stages[lives])

    if display.count("_") == 0:
        print("You win!")
        game_over = True
    elif lives == 0:
        print("You lost")
        game_over = True