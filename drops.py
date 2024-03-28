import turtle 
import random
from window import LEFT, GUTTER, RIGHT, TOP


drop_type = {
    1: 'mini_pal', # shape triangle
    2: 'through',  # shape circle
    3: 'faning',   # shape square 
    4: 'bomb'      # shape classic
}

drops = []
def create_drop(wasp):
    drop = turtle.Turtle()
    drop.penup()
    drop.turtlesize(1.5)

    # drop the item at the wasp location
    pos = wasp.pos()
    drop.setposition(pos)

    # each type has equal probability to appear
    dtype = random.randint(1, 4)
    if dtype == 1:
        drop.shape("triangle")
        drop.color("Salmon")
    elif dtype == 2:
        drop.shape("circle")
        drop.color("SpringGreen")
    elif dtype == 3:
        drop.shape("square")
        drop.color("DeepSkyBlue")
    else:
        drop.shape("classic")
        drop.color("AliceBlue")

    drop.setheading(-90)
    drops.append(drop)