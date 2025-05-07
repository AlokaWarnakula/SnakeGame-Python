from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #  food detected
    if snake.head.distance(food) < 13:
        food.refresh()
        snake.grow()
        scoreBoard.addScore()

    #  hit wall detections
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # if 280 can't turn near the wall
        scoreBoard.hitWall()
        gameOn = False

    #  detected head collide with body part
    for bodyPart in snake.segments[2:]:
        if snake.head.distance(bodyPart) < 10:
            scoreBoard.hitBody()
            gameOn = False

screen.exitonclick()
