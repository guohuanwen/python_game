# coding=utf-8
import cocos
from cocos.actions import *


class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super(HelloWorld, self).__init__()
        label = cocos.text.Label(
            'Hello, world',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        label.position = 320, 240
        self.add(label)


class BaseSprite(cocos.layer.ColorLayer):
    def __init__(self):
        super(BaseSprite, self).__init__(64, 64, 224, 255)
        lable = cocos.text.Label(
            'hello world',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        lable.position = 320, 240
        self.add(lable)
        sprite = cocos.sprite.Sprite('apple.png')
        sprite.position = 320, 240
        sprite.scale = 3
        self.add(sprite, z=1)
        scale = ScaleBy(3, duration=3)
        lable.do(Repeat(scale + Reverse(scale)))
        sprite.do(Repeat( Reverse(scale) + scale ))


cocos.director.director.init()
# helloworld = HelloWorld()
# main_scene = cocos.scene.Scene(helloworld)
baseSprite = BaseSprite()
baseSprite.do(JumpBy( (200,0), 50,3,5))
main_scene = cocos.scene.Scene(baseSprite)
cocos.director.director.run(main_scene)
