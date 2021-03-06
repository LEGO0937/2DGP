from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

#frame = 0
#direction = 100

def go_point1_to_point2():
    x, y = 203, 535
    frame = 0
    direction = 0
    while x > 132 and y > 243:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, direction, 100, 100, x, y)
        update_canvas()
        frame = (frame+1) % 8
        x -= 3
        y -= 21
        delay(0.1)
        get_events()

def go_point2_to_point3():
    x, y = 132, 243
    frame = 0
    direction = 100
    while x < 535 and y < 470:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, direction, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 37
        y += 20
        delay(0.1)
        get_events()

def go_point3_to_point4():
    x, y =  535, 470
    frame = 0
    direction = 0
    while x > 477 and y > 203:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, direction, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 3
        y -= 13
        delay(0.1)
        get_events()
def go_point4_to_point5():
    x, y = 477, 203
    frame = 0
    direction = 100
    while x < 715 and y > 136:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, direction, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 11
        y -= 3
        delay(0.1)
        get_events()

def go_point5_to_point6():
    x, y = 715, 136
    frame = 0
    direction = 0
    while x > 316 and y < 225:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, direction, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 13
        y += 3
        delay(0.1)
        get_events()
def go_point6_to_point7():
    x, y = 316, 225
    frame = 0
    direction = 100
    while x <510 and y > 92:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, direction, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 4
        y -= 3
        delay(0.1)
        get_events()

def go_point7_to_point8():
    x, y = 510, 92
    frame = 0
    direction = 100
    while x < 692 and y < 518:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, direction, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 4
        y += 10
        delay(0.1)
        get_events()
def go_point8_to_point9():
    x, y = 692, 518
    frame = 0
    direction = 0
    while x > 682 and y > 336:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, direction, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 1
        y -= 18
        delay(0.1)
        get_events()
def go_point9_to_point10():
    x, y = 682, 336
    frame = 0
    direction = 100
    while x < 712 and y < 349:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, direction, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 3
        y += 1
        delay(0.1)
        get_events()
def go_point10_to_point1():
    x, y = 712, 349
    frame = 0
    direction = 0
    while x > 203 and y < 535:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, direction, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 16
        y += 6
        delay(0.1)
        get_events()

while True:
    go_point1_to_point2()
    go_point2_to_point3()
    go_point3_to_point4()
    go_point4_to_point5()
    go_point5_to_point6()
    go_point6_to_point7()
    go_point7_to_point8()
    go_point8_to_point9()
    go_point9_to_point10()
    go_point10_to_point1()

#함수의 이름의 시작은 항상 동사(verb)로 한다


#아랫줄로 개행할 때 Shift+Enter키를 누르면 문장 중간에서 바로 개행된다
#코드 중간에 뜨는 회색줄은 프로그램이 돌아가는데 지장이 없는것들
#코드 중간에 뜨는 빨간줄은 그냥 에러
close_canvas()


