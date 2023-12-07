from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.color("blue")
        self.goto(0, 0)
        self.write(f"GAME OVER. Better Luck Next Time ", align=ALIGNMENT, font=FONT)

