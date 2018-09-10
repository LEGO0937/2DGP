from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 20
y = 90
while(True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if x < 778 and y == 90:
        x = x+2
    elif x == 778 and y < 560:
        y = y+2
    elif x > 20 and y == 560:
        x = x-2
    elif x == 20 and y > 90:
        y = y-2
    delay(0.01)
    
close_canvas()
