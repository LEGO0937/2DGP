from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def go_to_mouse_point(clickX, clickY):
    global char_x, char_y
    global plus_x, plus_y
    global direction
    plus_x, plus_y = clickX - char_x, clickY - char_y
    if char_x > click_x:
        direction = 0
    elif char_x < click_x:
        direction = 100
    char_x += plus_x // 10
    char_y += plus_y // 10


def handle_events():
    global running
    global x, y
    global click_x, click_y
    global stop_or_go
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            click_x, click_y = x, y
            if stop_or_go == True:
                stop_or_go = False
            elif stop_or_go == False:
                stop_or_go = True
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 -  event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



open_canvas(KPU_WIDTH, KPU_HEIGHT)
mouse = load_image('hand_arrow.png')
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
click_x, click_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
char_x, char_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
plus_x, plus_y = 0, 0
direction = 100
stop_or_go = False
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if stop_or_go == True or stop_or_go == False:
        go_to_mouse_point(click_x, click_y)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, char_x, char_y)
    mouse.draw(x + 26, y - 26)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)
    handle_events()

close_canvas()




