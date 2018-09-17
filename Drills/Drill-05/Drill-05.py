from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_from_center_to_right():
    x, y = 800 // 2, 90
    while x < 800 - 25:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x+=2
        delay(0.01)

def move_up():
    x, y = 800 - 25 // 2, 90
    while y < 600 - 50:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)

def move_left():
    x, y = 800 - 25 // 2, 600 - 50
    while x > 0 + 25 // 2:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)

def move_down():
    x, y = 0 // 2, 600 - 50
    while y > 0 + 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)

def move_from_left_to_center():
    x, y = 0 // 2, 0 + 90
    while x < 400 - 25:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)



def make_rectangle():
    #move_from_center_to_right()
    #move_up()
    #move_left()
    #move_down()
    move_from_left_to_center()

def make_circle():

    pass


while True:
    make_rectangle()
    make_circle()

#함수의 이름의 시작은 항상 동사(verb)로 한다


#아랫줄로 개행할 때 Shift+Enter키를 누르면 문장 중간에서 바로 개행된다
#코드 중간에 뜨는 회색줄은 프로그램이 돌아가는데 지장이 없는것들
#코드 중간에 뜨는 빨간줄은 그냥 에러
close_canvas()


