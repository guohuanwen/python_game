# coding=utf-8

from map import Map
from keyboard import *
import pyglet

class GameMain(cocos.layer.Layer):

    is_event_handler = True
    score = 0
    # bg = pyglet.resource.media('bg.mp3')
    jump = pyglet.resource.media('jump.wav')



    def __init__(self):
        super(GameMain, self).__init__()
        self.textLable = cocos.text.Label(u'分数：0',
                                          font_name=FONTS,
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
        self.bg_player = pyglet.media.Player()
        self.bg_player.queue(pyglet.resource.media('bg.mp3'))

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        # if self.is_run:
        #     self.sound_jump.play()
        if not self.is_run:
            self.bg_player.play()
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
        self.bg_player.delete()
        self.unschedule(self.refresh)
        self.is_run = False
        self.reset()

    def reset(self):
        self.map.reset()
        self.bird.reset()
        self.map.x = 0
        self.map.y = - MAP_HEIGHT / 2 + SCREEN_HEIGHT / 2
        self.bird.position = SCREEN_WIDTH / 2, MAP_HEIGHT / 2
        self.is_run = False
        self.bg_player.queue(pyglet.resource.media('bg.mp3'))


cocos.director.director.init(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, resizable=True)
scene = cocos.scene.Scene(GameMain())
cocos.director.director.run(scene)
