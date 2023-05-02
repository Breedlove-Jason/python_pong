from turtle import Screen
from paddles import Paddle
from ball import Ball
import time

HEIGHT = 600
WIDTH = 800

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.w_up, "w")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.s_down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()



screen.exitonclick()