from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.goto(-100, 230)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 230)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)
        
        
    def increase_left_score(self):
        self.left_score += 1
        self.update_score()
        
    def increase_right_score(self):
        self.right_score += 1
        self.update_score()