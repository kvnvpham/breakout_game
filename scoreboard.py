from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(-275, 340)

        self.high_score = 0
        self.score = 0
        self.lives = 3

    def display_stats(self):
        self.clear()
        self.pendown()
        self.write(f"High Score: {self.high_score}\n"
                   f"Score: {self.score}\n"
                   f"Lives:  {self.lives}",
                   align="left",
                   font=("Arial", 12, "normal")
                   )

    def display_win(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("You Win!",
                   align="center",
                   font=("Arial", 40, "normal")
                   )

    def display_lose(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("You Lose",
                   align="center",
                   font=("Arial", 40, "normal")
                   )

    def update_score(self, block):
        if block.fillcolor() == "blue":
            self.score += 1
        elif block.fillcolor() == "green":
            self.score += 2
        elif block.fillcolor() == "yellow":
            self.score += 3
        elif block.fillcolor() == "orange":
            self.score += 3
        else:
            self.score += 4

    def update_lives(self):
        self.lives -= 1

    def save_score(self):
        if self.score > self.high_score:
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.score))

    def load_score(self):
        try:
            with open("highscore.txt") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            pass
