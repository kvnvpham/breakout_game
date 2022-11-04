from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.goto(0, -250)

        self.move_distance = 30

    def move_left(self):
        if self.xcor() < -260:
            self.goto(x=self.xcor(), y=self.ycor())
        else:
            self.goto(x=self.xcor() - self.move_distance, y=self.ycor())

    def move_right(self):
        if self.xcor() > 260:
            self.goto(x=self.xcor(), y=self.ycor())
        else:
            self.goto(x=self.xcor() + self.move_distance, y=self.ycor())
