import turtle 
import random
from window import LEFT, GUTTER, RIGHT, TOP, FLOOR_LEVEL


pals = []
adjustments = [-50, 50]
fanning =  []
def create_mini_pals(pistol, pals):
    for i in range(2):
        pal = turtle.Turtle()
        pal.penup()
        pal.color(1, 1, 1)
        pal.shape('img/mini_pal.gif')
        pal.turtlesize(1, 1)
        pal.pistol_movement = 0 # -1, 0 or 1 for left, stationary, right
        pal.setposition(pistol.xcor() + adjustments[i], FLOOR_LEVEL)
        pals.append(pal)


def draw_pals(pistol):
    for i in range(2):
        pal = pals[i]
        pal.clear()
        pal.turtlesize(1, 1)
        pal.stamp()
        pal.setposition(pistol.xcor() + adjustments[i], FLOOR_LEVEL)

def remove_mini_pals(pals, window):
    for pal in pals.copy():
        pal.clear()
        pal.hideturtle()
        window.update()
        pals.remove(pal)
        turtle.turtles().remove(pal)




