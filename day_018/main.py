import random
import turtle as t
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

turtle = t.Turtle()
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.pensize(5)
t.colormode(255)

def random_color():
    color = random.choice(rgb_colors)
    tuple = (color.r, color.g, color.b)
    return tuple

def draw_circle():
    turtle.dot(15, random_color())

def draw_row(y):
    turtle.setposition(-325, y)
    for int in range(14):
        draw_circle()
        if (int != 13):
            turtle.forward(50)

y_cor = -300

while y_cor < 301:
    draw_row(y_cor)
    y_cor += 50

screen = t.Screen()
screen.exitonclick()