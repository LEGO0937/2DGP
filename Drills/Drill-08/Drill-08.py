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


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

point = [(random.randint(0 + 90, KPU_WIDTH - 90), random.randint(0 + 90, KPU_HEIGHT - 90)) for i in range(10)]

frame = 0
direction = 100

while True:

close_canvas()