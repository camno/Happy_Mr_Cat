# author: camno
# v0.8
import random
import time
import turtle
from pistol import *
from wasp import *
from laser import *
from window import *
from drops import *
from enhance import *
from parameter import *


# Create turtle for writing text
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.setposition(LEFT * 0.8, TOP * 0.8)
text.color(1, 1, 1)

# Create turtle for welcome text 
welcome = turtle.Turtle()
welcome.penup()
welcome.setposition(LEFT * 0.5, TOP * 0.5)
welcome.color(1,1,1)

draw_pistol()

# Game loop
wasp_timer = 0
game_timer = time.time()

# effect timers 
pal_timer = 0
through_timer = 0
fanning_timer = 0

#
score = 0
level = 1
game_running = True
restart = False
init = True

# enhance flags
mini_pals_on = False
through = False

while init:
    welcome.clear()
    welcome.write(
        f"Welcome Happy Mr. Cat, \nplease select your encounter now!\n\n\nNormal(n)         Hard(h)",
        font=("Courier", 24, "bold"),
    )
    
    difficult_level = window.textinput('Select Difficulty', "Please press n(Normal) or h(Hard) ")

    if difficult_level == 'n':
        WASP_SPEED = WASP_SPEED * 1
        WASP_SPAWN_INTERVAL = WASP_SPAWN_INTERVAL * 1
        init = False
    elif difficult_level == 'h':
        WASP_SPEED = WASP_SPEED * 1.5 
        WASP_SPAWN_INTERVAL = WASP_SPAWN_INTERVAL / 2
        init = False
    else:
        difficult_level = window.textinput('Select Difficulty', "Please press n(Normal) or h(Hard) ")

welcome.clear()
welcome.penup()
welcome.hideturtle()

# Key bindings
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeyrelease(stop_pistol_movement, "Left")
window.onkeyrelease(stop_pistol_movement, "Right")
window.onkeypress(create_laser, "space")
window.onkeypress(turtle.bye, "q")
window.listen()

while game_running:

    timer_this_frame = time.time()

    time_elapsed = time.time() - game_timer
    text.clear()
    text.write(
        f"Time: {time_elapsed:5.1f}s \nScore: {score:5} \nLevel: {level:5}",
        font=("Courier", 20, "bold"),
    )
    
    # Move pistol
    new_x = pistol.xcor() + PISTOL_STEP * pistol.pistol_movement
    if LEFT + GUTTER <= new_x <= RIGHT - GUTTER:
        pistol.setx(new_x)
        draw_pistol()
        # Move pals
        if mini_pals_on:
            draw_pals(pistol)
    
    # Move all lasers
    for laser in lasers.copy():

        move_laser(laser)

        # Remove laser if it goes off the screen
        if laser.ycor() > TOP:
            remove_sprite(laser, lasers, window)
            break

        # Check for collision with wasps
        for wasp in wasps.copy():           
            if laser.distance(wasp) < 50:
                # laser hit the wasp, 10% drop rate for enhance items(default)
                if random.random() < DROP_RATE:
                    create_drop(wasp)
                if through == False:
                    remove_sprite(laser, lasers, window)
                remove_sprite(wasp, wasps, window)
                # score depends on wasp types
                if wasp.shape() == "img/wasp0.gif":
                    score += 1
                elif wasp.shape() == "img/wasp1.gif":
                    score += 2
                elif wasp.shape() == "img/wasp2.gif":
                    score += 3
                else:
                    score += 4

                level = score // 100 + 1 
                break

    # Spawn new wasps when time interval elapsed
    if time.time() - wasp_timer > WASP_SPAWN_INTERVAL:
        create_wasp(wasps)
        wasp_timer = time.time()

    # remove effects when the time limit is reached
    # mini pals
    if mini_pals_on and (time.time() - pal_timer > EFFECT_TIME_LIMIT):
        remove_mini_pals(pals, window)
        mini_pals_on = False
    
    # through effect
    if through == True and (time.time() - through_timer > EFFECT_TIME_LIMIT):
        through = False
    
    # fanning out effect wear off
    if fanning and (time.time() - fanning_timer > EFFECT_TIME_LIMIT):
        fanning.pop()

    # Move all the drops
    for drop in drops:
        drop.forward(DROP_SPEED)
        # Remove drop if it goes off the screen
        if drop.ycor() < BOTTOM:
            remove_sprite(drop, drops, window)
            break 
        # check whether succefully collecting the drop item
        if drop.distance(pistol) < 25:
            # get the type of drops based on the turtle shape
            drop_shape = drop.shape()
            if drop_shape == "img/mini_pals.gif" and mini_pals_on == False: # drop item 1: summon mini guns 
                create_mini_pals(pistol, pals)
                mini_pals_on = True 
                pal_timer = time.time()
            elif drop_shape == "img/through.gif" and through == False: # drop item 2: enable the laser to go through wasps
                through = True
                through_timer = time.time()
            elif drop_shape == "img/fanning.gif" and not fanning: # drop item 3: fanning out the lasers
                fanning.append(True)
                fanning_timer = time.time()
            elif drop_shape == "img/bomb.gif": # drop item 4: bomb out all the wasps on screen at once
                for wasp in wasps.copy():
                    score += int(wasp.shapesize()[0]) 
                    level = score // 100 + 1
                    remove_sprite(wasp, wasps, window)

            remove_sprite(drop, drops, window)
            
            break 

    
    # Move all wasps
    for wasp in wasps:
        wasp.forward(WASP_SPEED)
        # Check for game over
        if wasp.ycor() < FLOOR_LEVEL:

            while True:
                try_again = window.textinput('You just died', "You're killed by wasps.\nWanna revenge?\nPlease press y(Yes) or n(No) ")
                if try_again not in ['n', 'y']:
                    continue
                else:
                    break 

            if try_again == 'n':
                game_running = False
                restart = False

            elif try_again == 'y':
                restart = True
                window.listen()
            break

    if restart == True:
        # remove all wasps for a restart
        for wasp in wasps.copy():
            remove_sprite(wasp, wasps, window)
        # clear the flying lasers in the field
        for laser in lasers.copy():
            remove_sprite(laser, lasers, window)
            
        window.update()
        wasp_timer = 0
        game_timer = time.time()
        score = 0
        restart = False

    time_for_this_frame = time.time() - timer_this_frame

    if time_for_this_frame < TIME_FOR_1_FRAME:
        time.sleep(TIME_FOR_1_FRAME - time_for_this_frame)
    
    window.update()

splash_text = turtle.Turtle()
splash_text.hideturtle()
splash_text.color(1, 1, 1)
splash_text.write("GAME OVER", font = ("Courier", 40, "bold"), align='center')

turtle.done()