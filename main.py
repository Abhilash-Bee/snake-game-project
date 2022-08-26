from turtle import Screen
from snake import *
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

snake_object = Snake()
food_object = Food()
score_board_object = ScoreBoard()

screen.listen()
screen.onkey(fun=snake_object.move_left, key="Left")
screen.onkey(fun=snake_object.move_right, key="Right")
screen.onkey(fun=snake_object.move_up, key="Up")
screen.onkey(fun=snake_object.move_down, key="Down")


def start_game(is_start):

    while is_start:
        time.sleep(0.1)
        screen.update()

        snake_object.move()
        # snake_object.move_forward()

        if snake_object.head.distance(food_object) < 15:
            snake_object.extend()
            score_board_object.increase_score()
            food_object.create_food()

        if snake_object.head.xcor() > 280 or snake_object.head.xcor() < -280 or snake_object.head.ycor() < -280 or \
                snake_object.head.ycor() > 280:
            score_board_object.game_over()
            is_start = False

        for snake in snake_object.snake[2:]:
            if snake_object.head.distance(snake) < 10:
                score_board_object.game_over()
                is_start = False


start_game(True)

screen.exitonclick()
