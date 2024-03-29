import turtle
from tkinter import PhotoImage    

def boundaries(window):
    LEFT = -window.window_width() / 2
    RIGHT = window.window_width() / 2
    TOP = window.window_height() / 2
    BOTTOM = -window.window_height() / 2
    FLOOR_LEVEL = 0.9 * BOTTOM
    GUTTER = 0.025 * window.window_width()
    return LEFT, RIGHT, TOP, BOTTOM, FLOOR_LEVEL, GUTTER

def remove_sprite(sprite, sprite_list, window):
    sprite.clear()
    sprite.hideturtle()
    window.update()
    sprite_list.remove(sprite)
    turtle.turtles().remove(sprite)


window = turtle.Screen()
window.tracer(0)
window.setup(0.3, 0.8)
window.bgcolor(0.2, 0.2, 0.2)
window.bgpic('img/background.gif')
window.title("Happy Mr. Cat")

# register wasps shapes
window.register_shape('img/wasp0.gif')
window.register_shape('img/wasp1.gif')
window.register_shape('img/wasp2.gif')
window.register_shape('img/wasp3.gif')
# register drop items shapes
window.register_shape('img/mini_pals.gif') # item 1
window.register_shape('img/through.gif') # item 2
window.register_shape('img/fanning.gif') # item 3
window.register_shape('img/bomb.gif') # item 4

# register laser gun 
window.register_shape('img/cat_gun.gif')

# register mini pal
window.register_shape('img/mini_pal.gif')

LEFT, RIGHT, TOP, BOTTOM, FLOOR_LEVEL, GUTTER = boundaries(window)
