# coding = utf-8

import cocos


class Pipe(cocos.sprite.Sprite):
    def __init__(self, is_up):
        if is_up:
            super(Pipe, self).__init__('pipe_down.png', position=(0, 0), anchor=(0, 0))
        else:
            super(Pipe, self).__init__('pipe_up.png', position=(0, 0), anchor=(0, 0))

    def update_x(self, position_x, map_x):
        if position_x + map_x < 0:
            self.x = self.x + 600
