# coding=utf-8
import cocos
from cocos.actions import *
import math


class Bird(cocos.sprite.Sprite):

    #重力加速度
    gravity = -1.5
    #起跳速度
    jump_velocity = 15

    def __init__(self):
        super(Bird, self).__init__('apple.png', position=(0, 0))
        self.last_x = -1
        self.last_y = -1
        self.move_x = 0
        self.move_y = 0
        self.velocity = 3.0
        self.direction = 0.0
        self.velocity_y = 0.0


    def drop(self):
        self.velocity_y = self.velocity_y + 0.5 * self.gravity

    def jump(self):
        self.velocity_y = self.jump_velocity


    def change_direction(self, key):
        if 65361 in key:  # 左
            self.direction = math.pi
        if 65362 in key:  # 上
            self.direction = math.pi / 2.0
        if 65363 in key:  # 右
            self.direction = 0.0
        if 65364 in key:  # 下
            self.direction = math.pi * 3 / 2.0

        if 32 in key:#空格
            self.direction = 0.0
            self.jump()




    def refresh(self):
        self.drop()
        if self.direction < 0:
            return
        else:
            self.x = self.x + math.cos(self.direction) * self.velocity
            self.y = self.y + self.velocity_y

        if self.last_x < 0:
            self.last_x = self.x
            self.last_y = self.y
        self.move_x = self.x - self.last_x
        self.move_y = self.y - self.last_y
        self.last_y = self.y
        self.last_x = self.x
