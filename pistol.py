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
    pistol.turtlesize(1, 4)  # Base
    pistol.stamp()
    pistol.sety(FLOOR_LEVEL + 10)
    pistol.turtlesize(1, 1.5)  # Next tier
    pistol.stamp()
    pistol.sety(FLOOR_LEVEL + 20)
    pistol.turtlesize(0.8, 0.3)  # Tip of pistol
    pistol.stamp()
    pistol.sety(FLOOR_LEVEL)


def move_left():
    pistol.pistol_movement = -1


def move_right():
    pistol.pistol_movement = 1


def stop_pistol_movement():
    pistol.pistol_movement = 0

# create pistol
pistol = pistol()