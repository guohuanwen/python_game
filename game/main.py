# coding=utf-8

from map import Map
from keyboard import *

class GameMain(cocos.layer.Layer):
    is_event_handler = True
    score = 0

    def __init__(self):
        super(GameMain, self).__init__()
        self.textLable = cocos.text.Label(u'分数：0',
                                          font_name='Times New Roman',
                                          font_size=16,
                                          anchor_x='center', anchor_y='center')
        self.textLable.position = 100, SCREEN_HEIGHT - + 100
        self.keys_pressed = set()
        self.bird = Bird()
        self.map = Map()
        self.map.x = 0
        self.map.y = - MAP_HEIGHT / 2 + SCREEN_HEIGHT / 2
        self.bird.position = SCREEN_WIDTH / 2, MAP_HEIGHT / 2
        self.add(self.map, z=0)
        # self.add(self.bird, z=1)
        self.map.add(self.bird, z=0)
        self.add(self.textLable, z=0)
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
        self.bird.refresh(dt)
        self.map.update(self.bird.move_x, self.bird.move_y)

        if self.bird.check_die(self.map.pipe1, self.map.pipe2):
            self.stop()

        if self.score != self.bird.x // SCREEN_WIDTH:
            self.score = self.bird.x // SCREEN_WIDTH
            self.textLable.element.text = u'分数：%d' % self.score

    def stop(self):
        self.unschedule(self.refresh)
        self.is_run = False
        # self.map.reset()
        # self.bird.reset()

cocos.director.director.init(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, resizable=True)
scene = cocos.scene.Scene(GameMain())
cocos.director.director.run(scene)
