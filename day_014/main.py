import random
import os
from art import logo, vs
from data import data

answer = True
correct = 0
user1 = random.choice(data)

def correctAnswer(user2):
    correct += 1
    return user2

while answer:
    os.system("clear")
    print(logo)
    print(f"Correct answers: {correct}")
    user2 = random.choice(data)

    print("Who has a higher follower count?")
    print(user1["name"] + " a " + user1['description'] + " in the " + user1['country'])
    print(vs)
    print(user2["name"] + " a " + user2['description'] + " in the " + user2['country'])
    choice = input(f"Type 'A' for {user1['name']} or type 'B' for {user2['name']}: ").lower()

    if (user1['follower_count'] == user2['follower_count']):
        correct += 1
        user1 = user2
    elif (user1['follower_count'] > user2['follower_count']):
        if (choice == 'a'):
            correct += 1
            user1 = user2
        else:
            print("That is incorrect")
            print(f"Final correct answers: {correct}")
            answer = False
    elif (user1['follower_count'] < user2['follower_count']):
        if (choice == 'b'):
            correct += 1
            user1 = user2
        else:
            print("That is incorrect")
            print(f"Final correct answers: {correct}")
            answer = False