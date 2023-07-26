##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import pandas
import sys
import random

my_email = "welch.charlie16@gmail.com"
password = "mxapieasxotsyvwe"

try:
    bdays = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("File (birthdays.csv) not found!")
    sys.exit()

today = dt.datetime.now()

for index, row in bdays.iterrows():
    if today.day == row.day and today.month == row.month:
        num = random.randint(1, 3)
        letter = f"letter_templates/letter_{num}.txt"
        try:
            with open(letter) as file:
                letter_text = file.read()
                mail = letter_text.replace("[NAME]", row.names)

                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(
                        from_addr=my_email, to_addrs=row.email, msg=mail
                    )
        except FileNotFoundError:
            print(f"File ({letter}) not found!")
            sys.exit()
