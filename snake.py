from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            self.add_snake(Turtle(), POSITIONS[i])

    def add_snake(self, new_snake, position):
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.setposition(position)
        self.snake.append(new_snake)

    def extend(self):
        last_snake_position = self.snake[-1].position()
        self.add_snake(Turtle(), last_snake_position)

    def move(self):
        for snake_at in range(len(self.snake) - 1, 0, -1):
            x_axis = self.snake[snake_at - 1].xcor()
            y_axis = self.snake[snake_at - 1].ycor()
            self.snake[snake_at].goto(x_axis, y_axis)
        self.head.forward(10)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
