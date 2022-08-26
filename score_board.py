from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setposition(0, 260)
        self.color("white")
        self.score = 0
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score:: {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="Game Over", align="center", font=("courier", 30, "bold"))
