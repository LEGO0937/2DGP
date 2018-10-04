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

    for i in range(0, 100, 2):
        t = i/100
        Char_X = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        Char_Y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        move_char((Char_X, Char_Y))


def curve_char(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    go_point_to_point(p10, p1, p2, p3)  # 점 1부터 2까지
    go_point_to_point(p1, p2, p3, p4)  # 점 2부터 3까지
    go_point_to_point(p2, p3, p4, p5)  # 점 3부터 4까지
    go_point_to_point(p3, p4, p5, p6)  # 점 4부터 5까지
    go_point_to_point(p4, p5, p6, p7)  # 점 5부터 6까지
    go_point_to_point(p5, p6, p7, p8)  # 점 6부터 7까지
    go_point_to_point(p6, p7, p8, p9)  # 점 7부터 8까지
    go_point_to_point(p7, p8, p9, p10)  # 점 8부터 9까지
    go_point_to_point(p8, p9, p10, p1)  # 점 9부터 10까지
    go_point_to_point(p9, p10, p1, p2)  # 점 10부터 1까지

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

point = [(random.randint(0 + 90, KPU_WIDTH - 90), random.randint(0 + 90, KPU_HEIGHT - 90)) for i in range(10)]

frame = 0
direction = 100

while True:
    curve_char(point[0], point[1], point[2], point[3], point[4], point[5], point[6], point[7], point[8], point[9])
close_canvas()