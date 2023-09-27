from ctypes import alignment
from turtle import Turtle

# constants
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_value = 0
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score_value}", move=False, align="center", font=FONT)

    def inc_score(self):
        self.score_value += 1
        self.clear()
        self.update_score()


class HighScore(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.h_score = 0
        self.goto(270, 270)
        self.update_score(self.h_score)

    def update_score(self, h_score):
        self.write(f"High Score: {h_score}", move=False, align="center", font=FONT)

    def show_hscore(self):
        if h_score >= Score.inc_score():
            h_score = self.score_value
            self.clear()
            self.update_score()
        self.clear()
        self.update_score()

    # def hscore(self):
    #     if self.high_score >= self.score_value:
    #         self.high_score = self.score_value
