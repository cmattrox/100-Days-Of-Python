from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=10, stretch_len=2)
        self.penup()
        self.goto(pos)
        
    
    def Up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def Down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)   