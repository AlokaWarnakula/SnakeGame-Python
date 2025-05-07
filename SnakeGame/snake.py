from turtle import Turtle
import random

INITIAL_POSITIONS = ((0, 0), (-20, 0), (-40, 0))  # constant variable name like this
# Color list for turtle blocks on black background
COLORS = [
    "red", "lime", "yellow", "cyan", "magenta", "orange",
    "deep pink", "turquoise", "gold", "chartreuse", "aqua",
    "blue", "violet", "purple", "spring green", "tomato",
    "dodger blue", "salmon", "medium slate blue", "green yellow"
]

MOVE_DISTANCE = 10

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # constructor
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            if i == 0:
                # head triangle
                aloka = Turtle()
                aloka.penup()
                aloka.color(random.choice(COLORS))
                aloka.shape("triangle")
                aloka.goto(INITIAL_POSITIONS[i])
                self.segments.append(aloka)
            # other parts square
            aloka = Turtle()
            aloka.penup()
            aloka.color(random.choice(COLORS))
            aloka.shape("circle")
            aloka.goto(INITIAL_POSITIONS[i])
            self.segments.append(aloka)

    def grow(self):
        aloka = Turtle()
        aloka.penup()
        aloka.color(random.choice(COLORS))
        aloka.shape("circle")
        last_segment = self.segments[-1]
        aloka.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(aloka)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_cod = self.segments[seg - 1].xcor()
            y_cod = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cod, y_cod)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
