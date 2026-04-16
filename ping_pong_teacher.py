from pygame import *

win_width = 700
win_height = 500
back =(100, 100,255)
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг Понг')
window.fill(back)
run = True
finish = False

class Game_Sprite(sprite.Sprite):
    def __init__(self,picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = w
        self.rect.h = h
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
 

class Player(Game_Sprite):
    def __init__(self, picture, w,h,x,y, speed_x, speed_y):
        super(). __init__(picture, w, h, x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

     def update_ball(self):
        self.rect.x += self.speed_x   
        if self.rect.x < 0 or self.rect.x > win_width - self.rect.w:
            self.speed_x *= -1    
        self.rect.y -= self.speed_y
        if self.rect.y < 0:
            self.speed_y *= -1
       

    def update_r(self): 
        keys = key.get_pressed()
        x, y = self.rect.x, self.rect.y 
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.h:
            self.rect.y += self.speed_y

    def update_l(self): 
        keys = key.get_pressed()
        x, y = self.rect.x, self.rect.y 
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed_y
        if keys[K_s] and self.rect.y < win_height - self.rect.h:
            self.rect.y += self.speed_y    

    

ball = Player('ball02.png',50, 50 , 200, 200, 10, 5)
player_l = Player('platform_v0.png',30, 150 , 0, 200, 0, 10)	 
player_r = Player('platform_v0.png',30, 150 , 670, 200, 0, 10)	


while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill(back)
    ball.reset()
    player_l.reset()    
    player_r.reset()     
    ball.update_ball()
    player_l.update_l()
    player_r.update_r()

    display.update()
