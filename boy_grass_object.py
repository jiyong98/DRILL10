import random

from pico2d import *

class bBool:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100, 700), 599
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= random.randint(1, 50)
        if self.y <= 70:
            self.y = 70
class sBool:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, 800), 599

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= random.randint(1, 70)

        if self.y <= 70:
            self.y = 70


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0, 7)
        self.x, self.y = random.randint(100, 800), 90
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 2
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# 초기화
open_canvas()
grass = Grass()
team = [Boy() for i in range(11)]
bbool = [bBool() for i in range(10)]
sbool = [sBool() for i in range(10)]
running = True

# loop
while running:
    handle_events()

    for boy in team:
        boy.update()
    for bool1 in sbool:
        bool1.update()
    for bool2 in bbool:
        bool2.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for bool1 in sbool:
        bool1.draw()
    for bool2 in bbool:
        bool2.draw()

    delay(0.07)
    update_canvas()
close_canvas()