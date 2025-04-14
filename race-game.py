from turtle import Turtle, Screen
import random

screen = Screen()
screen.listen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win the race?")
colors = ["red", "yellow", "green", "blue", "orange", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles=[]

race_start = False

for turtle_position in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_position])
    new_turtle.color(colors[turtle_position])
    all_turtles.append(new_turtle)

    
if user_bet:
    race_start = True
    
while race_start:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_start = False
            if user_bet == turtle.pencolor():
                print(f"You won!, the winning color is {turtle.pencolor()}")
            else:
                print(f"You lost!, the winning color is {turtle.pencolor()}")
    
        race_distance = random.randint(0,10)
        turtle.forward(race_distance)    




screen.exitonclick()