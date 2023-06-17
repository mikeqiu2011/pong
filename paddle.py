from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(350, 0)
        self.color('white')

    def go_up(self):
        if self.ycor() <= 220:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() >= -210:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)