from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


x = 0
y = 100
speed = 10
frame = 0
while (True):
    #x < 800
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, y, 100, 100, x, 90)
    update_canvas()
    if x >= 800:
        speed = -10
        y = 0
    elif x <= 0:
        speed = 10
        y = 100
    frame = (frame + 1) % 8
    x += speed
    delay(0.03)
    get_events()


#아랫줄로 개행할 때 Shift+Enter키를 누르면 문장 중간에서 바로 개행된다
#코드 중간에 뜨는 회색줄은 프로그램이 돌아가는데 지장이 없는것들
#코드 중간에 뜨는 빨간줄은 그냥 에러
close_canvas()


