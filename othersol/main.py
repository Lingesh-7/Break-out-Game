from turtle import Screen
from paddel import Paddle
from ball import Ball
import time
from blocks import Blocks
from score import ScoreBoard
from game_over import GameOver


screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

game_over = GameOver()
score = ScoreBoard()
paddle = Paddle((0, -280))
ball = Ball((0, -260))

red_blocks = []
yellow_blocks = []
blue_blocks = []
green_blocks = []
orange_blocks = []
purple_blocks = []
rounds = 3

for _ in range(7):
    block = Blocks((0, 0))
    red_blocks.append(block)

red_blocks[0].goto(-330, 200)
red_blocks[1].goto(-220, 200)
red_blocks[2].goto(-110, 200)
red_blocks[3].goto(-0, 200)
red_blocks[4].goto(110, 200)
red_blocks[5].goto(220, 200)
red_blocks[6].goto(330, 200)


for _ in range(7):
    block = Blocks((0, 0))
    block.color("yellow")
    yellow_blocks.append(block)

yellow_blocks[0].goto(-330, 140)
yellow_blocks[1].goto(-220, 140)
yellow_blocks[2].goto(-110, 140)
yellow_blocks[3].goto(-0, 140)
yellow_blocks[4].goto(110, 140)
yellow_blocks[5].goto(220, 140)
yellow_blocks[6].goto(330, 140)


for _ in range(7):
    block = Blocks((0, 0))
    block.color("blue")
    blue_blocks.append(block)

blue_blocks[0].goto(-330, 170)
blue_blocks[1].goto(-220, 170)
blue_blocks[2].goto(-110, 170)
blue_blocks[3].goto(-00, 170)
blue_blocks[4].goto(110, 170)
blue_blocks[5].goto(220, 170)
blue_blocks[6].goto(330, 170)

for _ in range(7):
    block = Blocks((0, 0))
    block.color("green")
    green_blocks.append(block)

green_blocks[0].goto(-330, 110)
green_blocks[1].goto(-220, 110)
green_blocks[2].goto(-110, 110)
green_blocks[3].goto(-00, 110)
green_blocks[4].goto(110, 110)
green_blocks[5].goto(220, 110)
green_blocks[6].goto(330, 110)


for _ in range(7):
    block = Blocks((0, 0))
    block.color("orange")
    orange_blocks.append(block)

orange_blocks[0].goto(-330, 80)
orange_blocks[1].goto(-220, 80)
orange_blocks[2].goto(-110, 80)
orange_blocks[3].goto(-00, 80)
orange_blocks[4].goto(110, 80)
orange_blocks[5].goto(220, 80)
orange_blocks[6].goto(330, 80)


for _ in range(7):
    block = Blocks((0, 0))
    block.color("purple")
    purple_blocks.append(block)

purple_blocks[0].goto(-330, 50)
purple_blocks[1].goto(-220, 50)
purple_blocks[2].goto(-110, 50)
purple_blocks[3].goto(-00, 50)
purple_blocks[4].goto(110, 50)
purple_blocks[5].goto(220, 50)
purple_blocks[6].goto(330, 50)


screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

is_on = True

def play_game():
    global rounds, is_on
    while is_on:
        screen.update()
        time.sleep(ball.move_speed)
        screen.update()
        ball.move_ball()

        #   Detect collision with the wall
        if ball.xcor() > 430 or ball.xcor() < -430:
            ball.bounce_x()
        if ball.ycor() > 280:
            ball.bounce_y()
        #   Detect collision with the paddle
        if ball.distance(paddle) < 50 and ball.ycor() < -250:
            ball.bounce_y()
          
        # Detect Collision with the blocks
        for i in red_blocks + yellow_blocks + blue_blocks + green_blocks + orange_blocks + purple_blocks :
            screen.update()
            if i in red_blocks:
                if ball.distance(i) < 50:
                    screen.update()
                    i.goto(3000, 3000)
                    ball.bounce_y()
                    score.double_point()

            else:
                if ball.distance(i) < 50:
                    screen.update()
                    i.goto(3000, 3000)
                    ball.bounce_y()
                    score.point()

        # Detect if the paddle misses
        if ball.ycor() < -280:
            rounds -= 1
            ball.reset_position()
            paddle.reset_position()
            score.highest_point()

            if rounds == 0:
                game_over.game_over()
                is_on = False


play_game()

screen.exitonclick()