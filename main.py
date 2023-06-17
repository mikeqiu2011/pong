from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
screen.listen()

r_paddle = Paddle()

screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()