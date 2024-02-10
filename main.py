from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Down", fun=snake.move_down)
screen.onkeypress(key="Left", fun=snake.move_left)
screen.onkeypress(key="Right", fun=snake.move_right)

screen.update()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        score.refresh_score()
        snake.add_turtle()

    # detect collision with wall
    if (snake.turtles[0].xcor() > 280 or snake.turtles[0].ycor() > 280 or snake.turtles[0].xcor() < -280 or
            snake.turtles[0].ycor() < -280):
        score.game_over()
        game_is_on = False

    # detect collision with tail
    for turtle in snake.turtles:

        if turtle == snake.turtles[0]:
            pass

        elif snake.turtles[0].distance(turtle) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
