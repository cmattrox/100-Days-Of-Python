from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = letters + symbols + numbers

    password = [
        random.choice(password_list)
        for _ in range(nr_letters + nr_symbols + nr_numbers)
    ]

    random.shuffle(password_list)

    res = "".join(password)

    password_entry.delete(0, "end")
    password_entry.insert(0, res)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_credentials():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": username, "password": password}}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(
            title=None, message="Please make sure to fill out all fields."
        )
    else:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search_password():
    service = website_entry.get()
    with open("passwords.json", "r") as file:
        data = json.load(file)

        try:
            email = data[service]["email"]
            password = data[service]["password"]
            messagebox.showinfo(
                title=None, message=f"Email: \n {email} \n Password: \n {password}"
            )
        except ValueError:
            messagebox.showerror(title=None, message="Please enter a valid service.")
        except KeyError:
            messagebox.showerror(
                title=None, message=f"{service} service does not exist."
            )


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website/Service: ", width=20)
website_label.grid(row=1, column=0)
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
search_button = Button(text="Search", command=search_password, width=13)
search_button.grid(row=1, column=2)

username_label = Label(text="Email/Username: ", width=20)
username_label.grid(row=2, column=0)
username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(index=0, string="welch.charlie16@gmail.com")

password_label = Label(text="Password: ", width=20)
password_label.grid(row=3, column=0)
password_entry = Entry(width=21, show="*")
password_entry.grid(row=3, column=1)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_credentials)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
