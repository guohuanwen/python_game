import cocos
from game_config import *
from bird import Bird
import cocos
from dot import Dot


class Map(cocos.layer.ColorLayer):
    def __init__(self):
        self.width = MAP_WIDTH
        self.height = MAP_HEIGHT
        super(Map, self).__init__(64, 64, 224, 255, width=self.width, height=self.height * 10)
        self.center = (self.width / 2, self.height / 2)
        self.random_point()

    def update(self, x, y):
        self.x = self.x - x
        self.y = self.y - y

    def random_point(self):
        i = 0
        while i < 500:
            self.add(Dot())
            i += 1
