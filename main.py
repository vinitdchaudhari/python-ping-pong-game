from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

paddle = Turtle()
screen = Screen()
score=Score()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))

screen.listen()
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() - 320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

    screen.update()
screen.exitonclick()
