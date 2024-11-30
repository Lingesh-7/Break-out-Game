from turtle import Turtle 
import random as r

COLORS=['red','orange','yellow','green']
LEVEL=[90,150,210,260]

class Bricks:
    def __init__(self):
        self.bricks=[]
        i=0
        while i<=3:
            for j in range(-250,250,60):
                brick=Turtle('square')
                brick.shapesize(stretch_len=5,stretch_wid=3)
                brick.color(COLORS[i])
                brick.penup()
                brick.goto(j,LEVEL[i])
                self.bricks.append(brick)
            i+=1

        # for i in range(-250,250,10):
        #     new=Turtle('square')
        #     new.shapesize(stretch_len=3,stretch_wid=1)
        #     new.color(COLORS[3])
        #     new.goto(i,150)
    # def bricks_in_row(self):

        # new=Turtle('square')
        # new.shapesize(stretch_len=3,stretch_wid=1)
        # new.penup()
        # new.color(COLORS[3])
        # randy= r.randint(-250,250)
        # new.goto(300,randy)
        # self.bricks.append(new)
    
    # def show_bricks(self):
    #     for j in range(len(LEVEL)):
    #         for i in range(-250,250,70):
    #             new=Turtle('square')
    #             new.penup()
    #             new.shapesize(stretch_len=3,stretch_wid=1)
    #             new.color(COLORS[j])
    #             new.goto(i,LEVEL[j])
    #             new.penup()
    #             self.bricks.append(new)

    # def return_bricks(self):
    #     return self.bricks
        
        