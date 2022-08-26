from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed(0)
        self.create_food()

    def create_food(self):
        self.clear()
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)


