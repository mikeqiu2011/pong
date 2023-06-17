import time
from turtle import Screen
from score_board import ScoreBoard

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')

screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

score_board = ScoreBoard()


def new_match():

    ball.refresh()

    game_is_on = True
    while game_is_on:
        time.sleep(.1)
        screen.update()
        ball.move()

        # detect if hit wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            print('ball hit wall')
            ball.bounce_by_wall()

        # detect if hit the right paddle
        if ball.xcor() > 330:
            if r_paddle.ycor() - 50 < ball.ycor() < r_paddle.ycor() + 50:
                print('right paddle caught the ball')
                ball.bounce_by_paddle()
            else:
                print('right paddle missed')
                score_board.l_score += 1
                game_is_on = False

        if ball.xcor() < -330:
            if l_paddle.ycor() - 50 < ball.ycor() < l_paddle.ycor() + 50:
                print('left paddle caught the ball')
                ball.bounce_by_paddle()
            else:
                print('left paddle missed')
                score_board.r_score += 1
                game_is_on = False

        score_board.refresh()

while True:
    new_match()


screen.exitonclick()