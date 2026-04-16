from pygame import *

win_width = 700
win_height = 500
back =(100, 100,255)
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг Понг')
window.fill(back)
run = True
finish = False

font.init()
font = font.Font(None, 30)
score_l = font.render('SCORE_L: 0', True, (255, 255, 255))
win_l = font.render('PLAYER L WIN!', True, (180, 0, 0))
score_r = font.render('SCORE_R: 0', True, (180, 0, 0))
win_r = font.render('PLAYER R WIN!', True, (180, 0, 0))
count_l = 0
count_r = 0

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
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > win_height - self.rect.h:
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

    def colliderect(self, rect):
       return self.rect.colliderect(rect)


    

ball = Player('ball02.png',50, 50 , 200, 200, 5, 5)
player_l = Player('platform_v2.png',30, 150 , 0, 200, 0, 10)	 
player_r = Player('platform_v2.png',30, 150 , 670, 200, 0, 10)	


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
    if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
        ball.speed_x *= -1

    window.blit(score_l, (20, 20))

    display.update()
