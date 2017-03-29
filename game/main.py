# coding=utf-8

from map import Map
from keyboard import *


class GameMain(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(GameMain, self).__init__()
        self.keys_pressed = set()
        self.bird = Bird()
        self.map = Map()
        self.map.x = - MAP_WIDTH / 2 + SCREEN_WIDTH / 2
        self.map.y = - MAP_HEIGHT / 2 + SCREEN_HEIGHT / 2
        self.bird.position = MAP_WIDTH / 2, MAP_HEIGHT / 2
        self.add(self.map, z=0)
        # self.add(self.bird, z=1)
        self.map.add(self.bird, z=0)
        self.is_run = False


    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        if not self.is_run:
            self.is_run = True
            self.schedule(self.refresh)
        # else:
        #     self.unschedule(self.refresh)
        #     self.is_run = False

        self.bird.change_direction(self.keys_pressed)

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)

    def refresh(self, dt):
        self.bird.refresh()
        self.map.update(self.bird.move_x, self.bird.move_y)


cocos.director.director.init(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, resizable=True)
scene = cocos.scene.Scene(GameMain())
cocos.director.director.run(scene)
