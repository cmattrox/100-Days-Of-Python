from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 9)

@app.route("/")
def home ():
    return ('<h1>Guess a number between 0 and 9!</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />')

@app.route("/<int:guess>")
def guess(guess):
    if guess < number:
        return "<h1>You're too low! Guess again.</h1>"
    if guess > number:
        return "<h1>You're too high! Guess again.</h1>"
    else:
        return "<h1>You got it right!</h1>"

if __name__ == "__main__":
    app.run(debug=True)