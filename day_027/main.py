from tkinter import *

window = Tk()
window.title("Fahrenheit to Celcius Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

# Instructions
header = Label(text="Input degrees of fahrenheit or celcius and \nclick convert to convert to the other degree.", font=("Arial", 36, "bold"))
header.grid(column=1, row=0)
header.config(padx=50, pady=50)

# Fahrenheit
f_label = Label(text="Fahrenheit:", font=("Arial", 24, "normal")) 
f_label.grid(column=0, row=1)

f_input = Entry()
f_input.grid(column=1, row=1)

# Celcius
c_label = Label(text="Celcius:", font=("Arial", 24, "normal"))
c_label.grid(column=0, row=2)

c_input = Entry()
c_input.grid(column=1, row=2)


# Convert
def convert():
    if len(f_input.get()) != 0:
        # Convert fahrenheit to celcius and input into c_input
        c_input.delete(0, len(c_input.get()) - 1)
        f = int(f_input.get())
        c = 5 / 9 * (f - 32)
        c_input.insert(0, c)
    elif len(c_input.get()) != 0:
        # Convert celcius to fahrenheit and input into f_input
        f_input.delete(0, len(f_input.get()) - 1)
        c = int(c_input.get())
        f = c * 9 / 5 + 32
        f_input.insert(0, f)
        

button = Button(text="Convert", font=("Arial", 24, "normal"), command=convert)
button.grid(column=1, row=3)

window.mainloop()