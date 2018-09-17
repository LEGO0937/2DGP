from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

#frame = 0
#direction = 100

def go_point1_to_point2():
    x, y = 203, 535
    frame = 0
    direction = 100
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
        x += 11
        y += 20
        delay(0.1)
        get_events()

def go_point3_to_point4():
    pass
def go_point4_to_point5():
    pass
def go_point5_to_point6():
    pass
def go_point6_to_point7():
    pass
def go_point7_to_point8():
    pass
def go_point8_to_point9():
    pass
def go_point9_to_point10():
    pass
def go_point10_to_point1():
    pass


while True:
    #go_point1_to_point2()
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


