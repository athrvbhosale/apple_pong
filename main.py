import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Apple Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 325 and ball.distance(r_paddle) < 40 or ball.xcor() < -325 and ball.distance(l_paddle) < 40:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()
        # ball.incr_speed()
        
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()
        # ball.incr_speed()

screen.exitonclick()