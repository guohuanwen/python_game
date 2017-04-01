from game_config import *
import cocos
from dot import Dot
from pipe import Pipe


class Map(cocos.layer.ColorLayer):
    def __init__(self):
        self.width = MAP_WIDTH
        self.height = MAP_HEIGHT
        super(Map, self).__init__(64, 64, 224, 255, width=self.width, height=self.height * 10)
        self.center = (self.width / 2, self.height / 2)

        self.pipe1 = Pipe()
        self.pipe2 = Pipe()
        self.pipe1.position = SCREEN_WIDTH / 2, MAP_HEIGHT / 2
        self.add(self.pipe1, z=0)
        self.add(self.pipe2, z=0)

    def update(self, x, y):
        self.x = self.x - x
        self.y = self.y - y
        self.pipe1.update_x(self.pipe1.position[0], self.x)


    def add_sprite(self):
        dot = Dot()
        dot.x = self.x
        dot.y = self.y
        self.add(dot)
