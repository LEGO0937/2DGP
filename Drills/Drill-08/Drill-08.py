from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 800





open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

point = [(random.randint(0 + 90, KPU_WIDTH - 90), random.randint(0 + 90, KPU_HEIGHT - 90)) for i in range(10)]

frame = 0
direction = 100

while True:

close_canvas()