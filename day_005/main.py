import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for x in range(nr_letters):
    ran_letter = random.randint(0, len(letters) - 1)
    password = password + letters[ran_letter]

for x in range(nr_symbols):
    ran_symbol = random.randint(0, len(symbols) - 1)
    password = password + symbols[ran_symbol]

for x in range(nr_numbers):
    ran_number = random.randint(0, len(numbers) - 1)
    password = password + numbers[ran_number]

ran_password = ""

for x in range(len(password)):
    ran_num = random.randint(0, len(password) - 1)
    ran_password += password[ran_num]
    password = password[:ran_num] + password[ran_num + 1:]

print(ran_password)