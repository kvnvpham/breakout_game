from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(x=0, y=100)

        self.x_move = 8
        self.y_move = -8
        self.move_speed = 0.03

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_ball(self):
        self.goto(x=0, y=100)

    def increase_speed(self):
        self.move_speed *= 0.93
