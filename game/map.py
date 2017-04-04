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

        self.pipe1 = Pipe(True)
        self.pipe2 = Pipe(False)
        self.pipe1.position = SCREEN_WIDTH, self.pipe2.height + 150
        self.pipe2.position = SCREEN_WIDTH, 0
        self.add(self.pipe1, z=0)
        self.add(self.pipe2, z=0)

    def update(self, x, y):
        self.x = self.x - x
        self.y = self.y - y

        self.pipe2.update_x(self.pipe1.position[0], self.x)
        self.pipe1.update_x(self.pipe1.position[0], self.x)


    def add_sprite(self):
        dot = Dot()
        dot.x = self.x
        dot.y = self.y
        self.add(dot)

    def reset(self):
        self.remove(self.pipe1)
        self.remove(self.pipe2)
        self.pipe1 = Pipe(True)
        self.pipe2 = Pipe(False)
        self.pipe1.position = SCREEN_WIDTH, self.pipe2.height + 150
        self.pipe2.position = SCREEN_WIDTH, 0
        self.add(self.pipe1, z=0)
        self.add(self.pipe2, z=0)

