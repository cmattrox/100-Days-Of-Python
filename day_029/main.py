from tkinter import *
from tkinter import messagebox
import random

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

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(
            title=None, message="Please make sure to fill out all fields."
        )
        is_ok = False
    else:
        is_ok = messagebox.askyesno(
            title=None,
            message=f"Is this all correct? \n\n \
            Website/Service: \n\
            {website}\n\n\
            Username/Email: \n\
            {username}\n\n\
            Password: \n\
            {password}\n",
        )

    if is_ok:
        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {username} | {password} \n")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


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
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

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
