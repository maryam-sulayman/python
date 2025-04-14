import turtle as t
from turtle import Turtle, Screen
import random


t.colormode(255)

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

timmy = Turtle()
screen = Screen()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(220)
timmy.forward(300)
timmy.setheading(0) 
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    timmy.forward(50)
    timmy.dot(20, random.choice(color_list))
    
    if dot_count % 10 == 0:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.left(180)



screen.exitonclick()