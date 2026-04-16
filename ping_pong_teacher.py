from pygame import *

win_width = 700
win_height = 500
back =(255,255,100)
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг Понг')
window.fill(back)
run = True
finish = False
score_l = 0
score_r = 0

font.init()
font1 = font.SysFont('verdana', 20)
font = font.SysFont('verdana', 50)
win_l = font.render('PLAYER L WIN!', True, (0, 255, 100))
win_r = font.render('PLAYER R WIN!', True, (0, 255, 100))
text_score_l = font1.render('SCORE L: '+ str(score_l), True, (0, 0, 180))
text_score_r = font1.render('SCORE R: '+ str(score_r), True, (0, 0, 180))
 
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


    

ball = Player('ball0.png',50, 50 , 200, 300, 5, 5)
player_l = Player('platform_v.png',30, 150 , 0, 200, 0, 10)	 
player_r = Player('platform_v.png',30, 150 , 670, 200, 0, 10)	


while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.fill(back)
        ball.reset()
        player_l.reset()    
        player_r.reset()     
        ball.update_ball()
        player_l.update_l()
        player_r.update_r()
        window.blit(text_score_r, (540, 20))
        window.blit(text_score_l, (40, 20))
        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            ball.speed_x *= -1
     
        if ball.rect.x > win_width:
            score_l += 1
            text_score_l = font1.render('SCORE L: '+ str(score_l), True, (0, 0, 180))
            ball.rect.x = 300
            ball.rect.y = 200            
            if score_l >= 3:             
                window.blit(win_l, (180, 200))            
                finish = True           

    display.update()
