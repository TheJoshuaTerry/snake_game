from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 22, 'normal')
with open('data.txt') as file:
    data = file.read()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(data)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def draw_line(self):
        self.goto(-300, 270)
        self.pendown()
        self.fd(600)
        self.penup()
        self.goto(-5, 270)

    def update_scoreboard(self):
        self.clear()
        self.draw_line()
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()