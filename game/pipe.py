#coding = utf-8

import cocos

class Pipe(cocos.sprite.Sprite):

    def __init__(self):
        super(Pipe, self).__init__('pipe_down.png', position=(0, 0))

    def update_x(self, position_x, map_x):
        print(position_x)
        print(map_x)
        if position_x + map_x < 0:
            self.position = self.position[0] + 600, self.position[1]