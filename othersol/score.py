from turtle import Turtle
with open("data.txt") as file:
    dada = int(file.read())

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.highest_score = dada
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 270)
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 270)
        self.write(f"Highest Score:{self.highest_score}", align=ALIGNMENT, font=FONT)


    def point(self):
        self.score += 1
        self.update_scoreboard()

    def double_point(self):
        self.score += 2
        self.update_scoreboard()

    def highest_point(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.update_scoreboard()
