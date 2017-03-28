import cocos
import pyglet
from game_config import *
from bird import *


class KeyBoard(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self):
        super(KeyBoard, self).__init__()
        self.textLable = cocos.text.Label("hello world", font_name='Times New Roman', font_size=32, x=MAP_WIDTH/2, y=MAP_HEIGHT/2)
        self.keys_pressed = set()
        self.update_text()
        self.add(self.textLable)

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.update_text()

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)
        self.update_text()

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string(k) for k in self.keys_pressed]
        text = 'key = '.join(key_names)
        self.textLable.element.text = text



