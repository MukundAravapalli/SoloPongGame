from turtle import Screen, tracer, Turtle
from random import Random
from paddle import Paddle
from ball import Ball
from score import Score, HighScore
import time

r = Random()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Solo Pong Game")
screen.tracer(0)

paddle1 = Paddle()
paddle2 = Paddle()
ball = Ball()
score = Score()
high_score = HighScore()


paddle1.make_paddle(350, 0)
# paddle2.make_paddle(-350, 0)

screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
# screen.onkey(paddle2.move_up, "s")
# screen.onkey(paddle2.move_down, "x")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.03)

    ball.move()

    # Detect collisions with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collisions with right paddel
    if ball.distance(paddle1) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        score.inc_score()

    # # Detect collisions with left paddel
    # if ball.distance(paddle2) < 50 and ball.xcor() < -320:
    #     ball.bounce_x()

    # Paddle misses the ball
    if ball.xcor() > 380:
        ball.goto(0, 0)
        score.score_value = 0
        score.clear()
        score.update_score()

    if score.score_value >= high_score.h_score:
        high_score.update_score(score.score_value)
        high_score.clear()
        high_score.h_score = score.score_value
        high_score.update_score(high_score.h_score)


screen.exitonclick()
