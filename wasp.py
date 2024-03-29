import turtle
import random
from window import LEFT, GUTTER, RIGHT, TOP


wasps = []
def create_wasp(wasps):
    wasp = turtle.Turtle()
    wasp.penup()
    wasp.setposition(
        random.randint(
            int(LEFT + GUTTER),
            int(RIGHT - GUTTER),
        ),
        TOP,
    )
    # random wasp types
    wtype = random.randint(1, 4)
    if wtype == 1:
        wasp.shape("img/wasp0.gif")
    elif wtype == 2:
        wasp.shape("img/wasp1.gif")
    elif wtype == 3:
        wasp.shape("img/wasp2.gif")
    else:
        wasp.shape("img/wasp3.gif")

    wasp.setheading(-90)
    wasp.color(random.random(), random.random(), random.random())
    wasps.append(wasp)