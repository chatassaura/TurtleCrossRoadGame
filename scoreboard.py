from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.goto(-270, 260)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.show()

    def show(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increment_lvl(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
