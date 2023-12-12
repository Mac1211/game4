from turtle import Screen
from stick import Stick
from ball import Ball 
from scoreboard import Scoreboard
import time

ball = Ball()
screen = Screen()
scoreboard = Scoreboard()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Welecome to pong')
screen.tracer(0)

r_stick = Stick(350,0)
l_stick = Stick(-350,0)

screen.listen()
screen.onkey(r_stick.go_up, 'Up')
screen.onkey(r_stick.go_down, 'Down')
screen.onkey(l_stick.go_up, 'w')
screen.onkey(l_stick.go_down, 's')

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.mov_speed)
    ball.refresh()
    if ball.ycor() == 280 or ball.ycor() == -280 :
        ball.bounce_y()
    if ball.distance(r_stick) < 50 and ball.xcor() > 320 or ball.distance(l_stick) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()