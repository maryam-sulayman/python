from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 23, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_board()
        
        
    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)    
        
        
    def reset(self):
       if self.score > self.high_score:
           self.high_score = self.score
       self.score = 0
       self.update_board()
        
    def increase_score(self):
        self.score += 1
        self.update_board()