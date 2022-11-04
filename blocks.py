from turtle import Turtle

POSITIONS = [
    [(-245, 120), (-175, 120), (-105, 120), (-35, 120), (35, 120), (105, 120), (175, 120), (245, 120)],
    [(-210, 160), (-140, 160), (-70, 160), (0, 160), (70, 160), (140, 160), (210, 160)],
    [(-245, 200), (-175, 200), (-105, 200), (-35, 200), (35, 200), (105, 200), (175, 200), (245, 200)],
    [(-210, 240), (-140, 240), (-70, 240), (0, 240), (70, 240), (140, 240), (210, 240)],
    [(-245, 280), (-175, 280), (-105, 280), (-35, 280), (35, 280), (105, 280), (175, 280), (245, 280)]
]

COLORS = ["blue", "green", "yellow", "orange", "red"]


class Blocks:

    def __init__(self):
        self.blocks = []

    def set_blocks(self):
        for i in range(len(POSITIONS)):
            for position in POSITIONS[i]:
                self.add_block(position, COLORS[i])

    def add_block(self, position, color):
        new_block = Turtle(shape="square")
        new_block.color(color)
        new_block.penup()
        new_block.turtlesize(stretch_wid=1, stretch_len=3)
        new_block.goto(position)
        self.blocks.append(new_block)

    def block_hit(self, block):
        block.hideturtle()
        self.blocks.remove(block)




