# coding=utf-8
import cocos
from cocos.actions import *


class Bird(cocos.sprite.Sprite):

    def __init__(self):
        super(Bird, self).__init__('apple.png', position=(0, 0))
        self.last_x = -1
        self.last_y = -1
        self.move_x = 0
        self.move_y = 0

    def jump(self):
        self.do(JumpBy((200, 0), 50, 3, 5))

    def refresh(self):
        if self.last_x < 0:
            self.last_x = self.x
            self.last_y = self.y
        self.move_x = self.x - self.last_x
        self.move_y = self.y - self.last_y
        self.last_y = self.y
        self.last_x = self.x
