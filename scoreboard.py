from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILE = 'score.txt'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.high_score = 0
        self.read_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.update_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_high_score(self):
        with open(FILE, mode='w') as temp:
            temp.write(str(self.high_score))

    def read_high_score(self):
        with open(FILE) as high_score:
            self.high_score = int(high_score.read())
