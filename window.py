import turtle     

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
window.setup(0.5, 0.75)
window.bgcolor(0.2, 0.2, 0.2)
window.title("The little wasps")

LEFT, RIGHT, TOP, BOTTOM, FLOOR_LEVEL, GUTTER = boundaries(window)
