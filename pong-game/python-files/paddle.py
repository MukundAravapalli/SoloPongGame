from turtle import Turtle

# Constants
MOVE_DISTANCE = 10


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        # self.make_paddle()

    def make_paddle(self, start_x, start_y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.right(-90)
        self.shapesize(stretch_len=4, stretch_wid=0.5)
        self.goto(start_x, start_y)
        self.speed("fastest")

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
