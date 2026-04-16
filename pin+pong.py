from pygame import *

win_weight = 700
win_height = 500
back = (100, 250, 150)
window = display.set_mode((win_weight, win_height))

display.set_caption('ping+pong')
window.fill(back)

run = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_size_x, player_size_y, player_speed ):
        super(). __init__()
        self.image = transform.scale(image.load(player_image), (player_size_x, player_size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update (self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
            
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill(back)

    time.delay(40)
    display.update()
