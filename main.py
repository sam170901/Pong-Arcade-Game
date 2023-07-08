from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

ball = Ball()

scoreboard = Scoreboard() 

screen.listen()
screen.onkey(r_paddle.goUp,"Up")
screen.onkey(r_paddle.goDown,"Down")
screen.onkey(l_paddle.goUp,"w")
screen.onkey(l_paddle.goDown,"s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect Collision with walls
    if (ball.ycor() > 275 or ball.ycor()<-275):
        ball.bounce_y()

    #Detect Collision with paddles
    if (ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.bounce_x()

    #Detect ball out of bounds
    if(ball.xcor()>380):
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update_score()

    if(ball.xcor()<-380):
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update_score()

        



screen.exitonclick()