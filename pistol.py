import turtle
from window import FLOOR_LEVEL

# Create laser pistol
def pistol():
    pistol = turtle.Turtle()
    pistol.penup()
    pistol.color(1, 1, 1)
    pistol.shape("square")
    pistol.setposition(0, FLOOR_LEVEL)
    pistol.pistol_movement = 0  # -1, 0 or 1 for left, stationary, right
    return pistol

def draw_pistol():
    pistol.clear()

    pistol.turtlesize(4, 1)  # Base
    pistol.stamp()
    pistol.sety(FLOOR_LEVEL)

    pistol.turtlesize(4.2, 0.3)  # Tip of pistol
    pistol.stamp()
    pistol.sety(FLOOR_LEVEL - 10)


def move_left():
    pistol.pistol_movement = -1


def move_right():
    pistol.pistol_movement = 1


def stop_pistol_movement():
    pistol.pistol_movement = 0

# create pistol
pistol = pistol()