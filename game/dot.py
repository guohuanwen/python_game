# coding=utf-8

import random
from cocos.sprite import Sprite
import game_config

class Dot(Sprite):
    def __init__(self, pos=None, color=None):
        if color is None:
            color = random.choice(game_config.ALL_COLOR)
        super(Dot, self).__init__('circle.png', color=color)

        if pos is None:
            self.position = (random.randint(40, game_config.MAP_WIDTH - 40),random.randint(40, game_config.MAP_HEIGHT - 40))
            self.scale = 0.8
        else:
            self.position = (pos[0] + random.random() * 32 - 16, pos[1] + random.random() * 32 - 16)
        self.schedule_interval(self.update, random.random() * 0.2 + 0.1)

    def update(self, dt):
        a = 1