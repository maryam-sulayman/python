from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("purple")
        self.penup()
        self.speed("fastest")
        self.refresh()
      
        
        
    def refresh(self):
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.goto(x_position, y_position)
