from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 800


def move_char(point):
    global frame
    clear_canvas()
    kpu.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, direction, 100, 100, point[0], point[1])
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.03)

def go_point_to_point(p1, p2, p3, p4):
    global direction
    i = 0

    if p2[0] < p3[0]:
        direction = 100
    elif p2[0] > p3[0]:
        direction = 0

    while True:
        t = i / 100
        Char_X = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        Char_Y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        move_char((Char_X, Char_Y))
        i = i + 2
        if 100 == i:
            break


def curve_char(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

point = [(random.randint(0 + 90, KPU_WIDTH - 90), random.randint(0 + 90, KPU_HEIGHT - 90)) for i in range(10)]

frame = 0
direction = 100

while True:

close_canvas()