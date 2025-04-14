from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Cup Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle =Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

ball = Ball()
scoreboard = Scoreboard()


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
        
    #Collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        
    
    #If right paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.increase_left_score()
    
    #If left paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.increase_right_score()









screen.exitonclick()
