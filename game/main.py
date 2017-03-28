from bird import Bird
import cocos
from game_config import *
from map import Map
from cocos.actions import *
from keyboard import *


class GameMain(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(GameMain, self).__init__()
        self.keys_pressed = set()
        self.bird = Bird()
        self.map = Map()
        self.bird.position = MAP_WIDTH / 2, MAP_HEIGHT / 2
        self.add(self.map, z=0)
        # self.add(self.bird, z=1)
        self.map.add(self.bird, z=0)
        self.is_run = False

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.bird.jump()
        if not self.is_run:
            self.is_run = True
            self.schedule(self.refresh)
        else:
            self.unschedule(self.refresh)
            self.is_run = False

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)

    def refresh(self, dt):
        self.bird.refresh()
        print(self.bird.move_x)
        self.map.update(self.bird.move_x, self.bird.move_y)


cocos.director.director.init(width=MAP_WIDTH, height=MAP_HEIGHT, resizable=True)
scene = cocos.scene.Scene(GameMain())
cocos.director.director.run(scene)
