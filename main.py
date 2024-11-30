from turtle import Turtle,Screen,mainloop,TurtleScreen
from paddel import Paddel
from ball import Ball
import time
from bricks import Bricks




my_screen=Screen()
my_screen.tracer(0)
my_screen.title("BreakOut Game 🎮")
my_screen.bgcolor('black')
my_screen.setup(height=600,width=500)
# screen=TurtleScreen(my_screen)


paddel_=Paddel((0,-250))
ball=Ball()
bricks_=Bricks()
# my_screen.update()

my_screen.listen()
my_screen.onkey(fun=paddel_.move_right,key='Right')
my_screen.onkey(fun=paddel_.move_left,key='Left')


game=0
score=0
# t=3
while True:
    time.sleep(ball.msp)
    my_screen.update()
    ball.move()


    #Wall Colidal
    

    if ball.ycor()>280:
        ball.bouncey()

    elif ball.xcor()<-230 or ball.xcor()>230:
        ball.bouncex()


    #paddel Codlidal
    if ball.distance(paddel_)<30 and ball.ycor()>-280:
        ball.bouncey()
    

    #collidal with bricks
    for i in range(len(bricks_.bricks)):
        if ball.distance(bricks_.bricks[i])<20:
            score+=1
            bricks_.bricks[i].ht()
            ball.bouncey()
        

    if ball.ycor()<-280:
        game+=1
        ball.resetp()
    
    if game==3:
        print(f"Your Score is {score}")
        break


my_screen.exitonclick()
# my_screen.mainloop()
# mainloop()