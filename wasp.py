import turtle
import random
from window import LEFT, GUTTER, RIGHT, TOP

wasps = []
def create_wasp(wasps):
    wasp = turtle.Turtle()
    wasp.penup()
    this_size = random.randint(1, 5)
    wasp.turtlesize(this_size)
    wasp.setposition(
        random.randint(
            int(LEFT + GUTTER),
            int(RIGHT - GUTTER),
        ),
        TOP,
    )
    wasp.shape("turtle")
    wasp.setheading(-90)
    wasp.color(random.random(), random.random(), random.random())
    wasps.append(wasp)