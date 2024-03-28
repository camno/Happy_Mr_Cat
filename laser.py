import turtle
from pistol import pistol
from parameter import LASER_LENGTH, LASER_SPEED
from enhance import *

lasers = []

def create_laser():

    # main pistol lasers
    laser = turtle.Turtle()
    laser.penup()
    laser.color(1, 0, 0)
    laser.hideturtle()
    laser.setposition(pistol.xcor(), pistol.ycor())
    laser.setheading(90)
    # Move laser to just above pistol tip
    laser.forward(20)
    # Prepare to draw the laser
    laser.pendown()
    laser.pensize(5)

    lasers.append(laser)
    
    if pals:
        for pal in pals:
            laser = turtle.Turtle()
            laser.penup()
            laser.color(1, 0, 0)
            laser.hideturtle()
            laser.setposition(pal.xcor(), pal.ycor())
            laser.setheading(90)
            # Move laser to just above pistol tip
            laser.forward(20)
            # Prepare to draw the laser
            laser.pendown()
            laser.pensize(5)
            lasers.append(laser)


    if fanning and len(pals) == 0:
            degrees = [-5, 5]
            for i in range(2):
                laser = turtle.Turtle()
                laser.penup()
                laser.color(1, 0, 0)
                laser.hideturtle()
                laser.setposition(pistol.xcor(), pistol.ycor())
                laser.setheading(90 + degrees[i])
                # Move laser to just above pistol tip
                laser.forward(20)
                # Prepare to draw the laser
                laser.pendown()
                laser.pensize(5)
                lasers.append(laser)


def move_laser(laser):
    laser.clear()
    laser.forward(LASER_SPEED)
    # Draw the laser
    laser.forward(LASER_LENGTH)
    laser.forward(-LASER_LENGTH)