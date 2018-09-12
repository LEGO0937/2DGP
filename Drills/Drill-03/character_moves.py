from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 20
y = 90
z = 0
direction = 0
theta = math.radians(2)
count = 0

while(True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if direction == 0:
        x = x+2
        if x >= 778:
            #x = x+2
            direction = 1
    elif direction ==1:
        y = y+2
        if y >= 560:
            #y = y+2
            direction = 2
    elif direction == 2:
        x = x-2
        if x <= 20:
            #x = x-2
            direction = 3
    elif direction == 3:
        y = y-2
        if y <= 90:
            #y = y-2
            direction = 4
    elif direction == 4:
        x = x+2
        if x >= 400:
            direction = 5
    elif direction == 5:
        x = x + (8 * math.cos(z))
        y = y + (8 * math.sin(z))
        z = z + theta
        count = count +1
        if count == 180:
            count = 0
            direction = 0
        
    delay(0.01)
    
close_canvas()
