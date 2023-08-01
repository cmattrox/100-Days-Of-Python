from tkinter import *
import time
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0

        self.window = Tk()
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.window.title("Quizzler")

        self.score_label = Label(
            text=f"Score: {self.score}", fg="white", bg=THEME_COLOR
        )
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.true = PhotoImage(file="./images/true.png")
        self.false = PhotoImage(file="./images/false.png")

        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
        )
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.get_next_question()

        self.false_button = Button(
            command=self.false_pressed, image=self.false, borderwidth=0
        )
        self.false_button.grid(column=1, row=2)
        self.true_button = Button(
            command=self.true_pressed, image=self.true, borderwidth=0
        )
        self.true_button.grid(column=0, row=2)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
