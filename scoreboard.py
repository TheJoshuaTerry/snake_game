from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 22, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.draw_line()
        self.hideturtle()
        self.update_scoreboard()

    def draw_line(self):
        self.goto(-300, 270)
        self.pendown()
        self.fd(600)
        self.penup()
        self.goto(-5, 270)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)