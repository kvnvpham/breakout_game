from turtle import Screen
from paddle import Paddle
from blocks import Blocks
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.tracer(0)

paddle = Paddle()
blocks = Blocks()
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(fun=paddle.move_left, key="Left")
screen.onkeypress(fun=paddle.move_right, key="Right")

scoreboard.load_score()
blocks.set_blocks()

game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()

    scoreboard.display_stats()
    ball.move()

    # Game End Conditions
    if ball.ycor() < -350:
        ball.reset_ball()
        if scoreboard.lives > 1:
            scoreboard.update_lives()
        else:
            scoreboard.save_score()
            scoreboard.display_lose()
            game_over = True

    if len(blocks.blocks) == 0:
        scoreboard.save_score()
        scoreboard.display_win()
        game_over = True

    # Ball Parameters
    if ball.ycor() > 380:
        ball.bounce_y()

    if ball.xcor() > 287 or ball.xcor() < -287:
        ball.bounce_x()

    if ball.distance(paddle) < 55 and -255 < ball.ycor() < -235:
        ball.bounce_y()
        ball.increase_speed()

    # Block Management
    for block in blocks.blocks:
        if ball.distance(block) < 33 and ball.ycor() > 115:
            blocks.block_hit(block)
            scoreboard.update_score(block)
            ball.bounce_y()

screen.exitonclick()
