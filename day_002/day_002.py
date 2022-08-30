print("Welcome to the tip calculator.")
bill = input("How much was the total bill? ")
people = input("How many people would you like to split the bill  between? ")
percent = input("Would you like to tip 18, 20 or 22 percent? ")

while(percent != "18" and percent != "20" and percent != "22"):
    print("Tip percent must be 18, 20 or 22 percent.")
    percent = input("Would you like to tip 18, 20 or 22 percent? ")

bill = float(bill)
people = int(people)
percent = int(percent)

percentage = percent / 100
total = bill * percentage + bill
final = total / people
final = str(final)

print("Each person should pay $" + final)