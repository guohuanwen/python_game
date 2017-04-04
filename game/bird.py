# coding=utf-8
import cocos
from cocos.actions import *
import math


class Bird(cocos.sprite.Sprite):

    #重力加速度
    gravity = -350
    #起跳速度
    jump_velocity = 300

    def __init__(self):
        super(Bird, self).__init__('apple.png', position=(0, 0), anchor=(0,0))
        self.last_x = -1
        self.last_y = -1
        self.move_x = 0
        self.move_y = 0
        self.velocity_x = 100.0
        self.direction = 0.0
        self.velocity_y = 0.0

    def drop(self, dt):
        self.velocity_y = self.velocity_y + self.gravity * dt

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

    def refresh(self, dt):
        self.drop(dt)
        if self.direction < 0:
            return
        else:
            self.x = self.x + self.velocity_x * dt
            self.y = self.y + self.velocity_y * dt

        if self.last_x < 0:
            self.last_x = self.x
            self.last_y = self.y
        self.move_x = self.x - self.last_x
        self.move_y = self.y - self.last_y
        self.last_y = self.y
        self.last_x = self.x

    def check_die(self, pipe1, pipe2):
        if self.x + self.width >= pipe1.x and self.x <= pipe1.x + pipe1.width:
            if self.y + self.height >= pipe1.y:
                print('die1')
                return True

        if self.x + self.width >= pipe2.x and self.x <= pipe2.x + pipe2.width:
            if self.y <= pipe2.y + pipe2.height:
                print(self.y)
                print(pipe2.y)
                print(pipe2.height)
                print('die2')
                return True

        if self.y <= pipe2.y:
            return True

        if self.y >= pipe1.y + pipe1.height:
            return True

        return False

    def reset(self):
        self.last_x = -1
        self.last_y = -1
        self.move_x = 0
        self.move_y = 0
        self.velocity_x = 100.0
        self.direction = 0.0
        self.velocity_y = 0.0