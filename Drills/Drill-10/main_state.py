import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state



name = "MainState"

boy = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        resume()
        self.frame = (self.frame + 1) % 8
        self.x += self.dir

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()


def exit():
    global boy, grass
    del (boy)
    del (grass)


def pause():
    boy.frame = boy.frame
    boy.x = boy.x


def resume():
    if boy.x >= 800:
        boy.dir = -1
    elif boy.x <= 0:
        boy.dir = 1


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            pause()



def update():
    boy.update()


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()





