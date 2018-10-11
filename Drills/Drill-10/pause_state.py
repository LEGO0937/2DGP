import game_framework
from pico2d import *
import main_state


name = "PauseState"
image = None


def enter():
    global image
    global button
    if button == 0:
        image = load_image('pause1.png')
    else:
        image = load_image('pause2.png')


def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s) or (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
                main_state.resume()


def draw():
    global frame
    global button
    global cnt
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    if button == 0:
        cnt += 1
        if cnt % 10 == 0:
            frame = (frame + 1) % 2
        image.clip_draw(frame * 512, 0, 512, 512, 400, 300)
    elif button == 1:
        frame = 0
        image.clip_draw(frame * 512, 0, 800, 600, 400, 300)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass

frame = 0
button = 0
cnt = 0



