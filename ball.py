import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.setheading(random.randint(20, 45))
        # self.setheading(75)

    def refresh(self):
        self.goto(0, 0)
        self.setheading(180 + self.heading())

    def move(self):
        self.forward(20)

    def bounce_by_wall(self):
        pre_heading = self.heading()
        self.setheading(360 - pre_heading)

    def bounce_by_paddle(self):
        pre_heading = self.heading()
        self.setheading(180 - pre_heading)



# heading - 270