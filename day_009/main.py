import os
from art import logo

print(logo)

new_user = "y"
user_dictionary = {}

while new_user == "y":
    name = input("What is the bidder's name?\n")
    bid = int(input("What is your bid? $"))

    user_dictionary[name] = bid

    new_user = input("Is there another bidder? [y/n] ")

    if new_user == "y":
        os.system('clear')

highest_bidder = max(user_dictionary, key=user_dictionary.get)
print(f"The highest bidder was {highest_bidder} with a bid of ${user_dictionary[highest_bidder]}")