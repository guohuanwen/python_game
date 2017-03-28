import cocos
from game_config import *
from bird import Bird


class Map(cocos.layer.ColorLayer):
    def __init__(self):
        self.width = MAP_WIDTH * 10
        self.height = MAP_HEIGHT * 10
        super(Map, self).__init__(64, 64, 224, 255, width=self.width, height=self.height * 10)
        self.center = (self.width / 2, self.height / 2)

    def update(self, x, y):
        self.x = self.x - x
        self.y = self.y - y
