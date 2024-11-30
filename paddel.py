from turtle import Turtle

class Paddel(Turtle):
    def __init__(self,cordinates):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.penup()
        self.goto(cordinates)


    def move_right(self):
        self.x_=self.xcor()+20
        # self.right
        self.goto(self.x_,self.ycor())
    

    def move_left(self):
        self.x_=self.xcor()-20
        self.goto(self.x_,self.ycor())
