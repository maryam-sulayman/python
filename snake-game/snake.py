from turtle import Turtle

STARTING_POSITIONS = [ (0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
     
     def __init__(self):
          self.snakes = []
          self.create_snake()
          self.head = self.snakes[0]
     
     
     def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)
            
                   
     def add_snake(self, position):
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snakes.append(snake)
            
     def extend(self):
         self.add_snake(self.snakes[-1].position())
          
            
     def move(self):
        for snake_position in range(len(self.snakes) -1, 0, -1): #range(start=2, stop=0, step=-1) => going from last to first
            new_x = self.snakes[snake_position -1].xcor()
            new_y = self.snakes[snake_position -1].ycor()
            self.snakes[snake_position].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
     def reset(self):
        for snake in self.snakes:
             snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]
        
    
     def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
        
     def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
     
     
     def left(self):
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)
     
     
     def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    