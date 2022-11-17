from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
on_break = False
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global on_break

    window.after_cancel(timer)
    title_label.config(text="Pomodoro\nTimer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    on_break = False
    checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global on_break

    if not on_break:
        title_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)
        on_break = True
    elif reps != 3:
        title_label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
        reps += 1
        on_break = False
    else:
        title_label.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
        reps = 0
        on_break = False

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer

    count_min = format(math.floor(count / 60), "02")
    count_sec = format(count % 60, "02")
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if (count > 0):
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps):
            mark += "✓"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)

title_label = Label(text="Pomodoro\n Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(window, text="Start", font=(FONT_NAME, 24, "normal"), highlightthickness=0, bg=RED, fg=PINK, bd=0, activebackground=RED, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(window, text="Reset", font=(FONT_NAME, 24, "normal"), highlightthickness=0, bg=RED, fg=PINK, bd=0, activebackground=RED, command=reset_timer)  
reset_btn.grid(column=2, row=2)

checkmark_label = Label(text="Cycles completed:", fg=RED, bg=YELLOW, font=(FONT_NAME, 24, "normal"))
checkmark_label.grid(column=1, row=3)

checkmark = Label(font=(FONT_NAME, 36, "normal"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=4)

window.mainloop()