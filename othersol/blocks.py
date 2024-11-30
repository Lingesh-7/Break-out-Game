from turtle import Turtle


class Blocks(Turtle):

    def __init__(self, position):

        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("red")
        self.penup()
        self.goto(position)

        # Defining borders of the brick
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15