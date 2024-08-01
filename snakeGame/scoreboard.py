from turtle import Turtle

FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.highest_score = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highest_score} ", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
            if self.score > self.highest_score:
                self.highest_score = self.score
                with open('data.txt', mode='w') as file:
                     file.write(str(self.highest_score))
                
            self.score = 0
            self.update_score()    

    def increase_score(self):
        self.score += 1
        self.update_score()

       
        
        
       


     