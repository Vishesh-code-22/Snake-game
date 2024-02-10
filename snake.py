from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.x = 20
        self.turtles = []
        for i in range(3):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            self.x -= 20
            new_turtle.goto(self.x, 0)
            self.turtles.append(new_turtle)

    def move(self):
        for t in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[t - 1].xcor()
            new_y = self.turtles[t - 1].ycor()
            self.turtles[t].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)

    def add_turtle(self):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("square")
        new_turtle.color("white")
        x = self.turtles[len(self.turtles)-1].xcor()
        y = self.turtles[len(self.turtles)-1].ycor()
        new_turtle.goto(x, y)
        self.turtles.append(new_turtle)

    def move_up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def move_down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def move_left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def move_right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

