from pygame import *

win_weight = 700
win_height = 500
back = (100, 250, 150)
window = display.set_mode((win_weight, win_height))

display.set_caption('ping+pong')
window.fill(back)

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill(back)

    time.delay(40)
    display.update()
