from turtle import Turtle
FONT = ("Courier", 100, "normal")
ALIGNMENT = "center"


class GameOver(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()

    def game_over(self):
        self.clear()
        self.goto(-10, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)