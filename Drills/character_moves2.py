from pico2d import *
import math



open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
z = 0
theta = math.radians(2)

while(True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x = x + (8 * math.cos(z))
    y = y + (8 * math.sin(z))
    z = z + theta
    delay(0.01)
    
close_canvas()
