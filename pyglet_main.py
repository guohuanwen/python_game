import pyglet
from pyglet.window import key
from pyglet.window import mouse
import cocos

window = pyglet.window.Window()

label = pyglet.text.Label('hello world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2,y=window.height//2,
                          anchor_x='center',anchor_y='center')

image = pyglet.resource.image("apple.png")


@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(window.width//3,window.height//3)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print 'The "A" key was pressed.'
        label.text = 'A'
    elif symbol == key.LEFT:
        print 'The left arrow key was pressed.'
    elif symbol == key.ENTER:
        print 'The enter key was pressed.'


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print 'The left mouse button was pressed.'

music = pyglet.resource.media('bg.mp3')
music.play()


pyglet.app.run()