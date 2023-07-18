from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

# ---------------------------- DATA INITIALIZATION ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_image, image=front_card)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=back_card)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def correct_answer():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("French Flashcards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=562)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"), fill="black"
)
card_word = canvas.create_text(
    400, 263, text="", font=("Ariel", 60, "bold"), fill="black"
)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=0)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(command=next_card, image=wrong_image, borderwidth=0)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(command=correct_answer, image=right_image, borderwidth=0)
right_button.grid(column=2, row=1)

next_card()

window.mainloop()
