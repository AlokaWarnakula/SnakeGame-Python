from turtle import Turtle

ALIGN = 'center'
FONT = ('Comic Sans MS', 20, 'bold')
LOSE = ('Comic Sans MS', 40, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)  # title location
        self.writingScore()

    def addScore(self):
        self.score += 1
        self.clear()
        self.writingScore()

    def writingScore(self):
        score = self.score
        self.write(f"Total Score is: {score}", move=False, align=ALIGN, font=FONT)

    def hitWall(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.goto(0, 0)
        self.write("Hit the wall", move=False, align=ALIGN, font=LOSE)

    def hitBody(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.goto(0, 0)
        self.write("Hit the body", move=False, align=ALIGN, font=LOSE)
