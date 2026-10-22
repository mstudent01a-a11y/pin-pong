#vers 22102026

from pygame import *
from time import time as timer

win_width = 700
win_height = 500
back =(255,255,100)
text_color = (0, 50, 150)
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг Понг')
window.fill(back)
run = True
finish = False
score_l = 0
score_r = 0
#timer = 0
#timerS = 0
font.init()
#font1 = font.SysFont('verdana bold', 40)
#font = font.SysFont('verdana', 50)



#restart = font1.render('Хочешь начать заново - жми ПРОБЕЛ', True, text_color)
#fon = transform.scale(image.load('fon0.jpg'), (700, 500))
                      
class Game_Sprite(sprite.Sprite):
    def __init__(self,picture, w, h, x, y,speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(Game_Sprite):        
    
    def update_ball(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 500 - 50: #win_height - self.rect.h:
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

class Label():
    def __init__(self, x=0, y=0, w=1, h=1, color=back):
        self.rect = Rect(x, y, w, h)
        self.color = color
        
    def fill(self):
        draw.rect(window, self.color, self.rect)
        
    def set_text(self, text, fsize, tcolor):
        self.text = text        
        self.image = font.SysFont('verdana', fsize).render(text, True, tcolor)
      
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  

      
#win = Label(250, 250, 1, 1, WHITE)
#win.set_text('YOU WIN', 70, WHITE)

win_l = Label(180, 200, 1, 1, back)
win_l.set_text('PLAYER L WIN!', 50, text_color)
win_r = Label(180, 200, 1, 1, back)
win_r.set_text('PLAYER R WIN!', 50, text_color)
text_score_l = Label(40, 10, 1,1, back)
text_score_l.set_text('SCORE L: '+ str(score_l), 30, text_color)
text_score_r = Label(500, 10, 1,1, back)
text_score_r.set_text('SCORE R: '+ str(score_r), 30, text_color)
text_timer = Label(300, 420, 1,1, back)
text_timer.set_text('Time: '+ '0', 30, text_color)
restart = Label(150, 470, 1,1,back)
restart.set_text('Хочешь начать заново - жми ПРОБЕЛ', 20, text_color)    
    

ball = Player('ball_p.png',50, 50 , 200, 300, 10, 10)
player_l = Player('platform_v.png',30, 150 , 0, 200, 0, 10)	 
player_r = Player('platform_v.png',30, 150 , 670, 200, 0, 10)	
#fon = Game_Sprite('fon0.jpg', 700, 500, 0, 0, 0, 0)
start_time = timer()
cur_time = start_time

while run:
    
    time.delay(60)
    display.update()

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                score_l = 0
                score_r = 0
                text_score_l.set_text('SCORE L: '+ str(score_l), 30, text_color)
                text_score_r.set_text('SCORE R: '+ str(score_r), 30, text_color)
                start_time = timer()
                cur_time = start_time
                text_timer.set_text('Time: '+ '0', 30, text_color)
                #time.delay(1000)
                finish = False
    
    if not finish:
        window.fill(back)
        #window.blit(fon, (0, 0))
        #fon.reset()
        ball.reset()
        player_l.reset()    
        player_r.reset() 
        ball.update_ball()
        player_l.update_l()
        player_r.update_r()   
        text_score_l.draw()  
        text_score_r.draw()
        text_timer.draw()
        
        new_time = timer()
        if new_time - cur_time > 1:
            cur_time = new_time
            text_timer.set_text('Time: '+ str(int(new_time - start_time)), 30, text_color)
            
        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            ball.speed_x *= -1

        if ball.rect.x < 0:
            score_r += 1
            text_score_r.set_text('SCORE R: '+ str(score_r), 30, text_color)
            ball.rect.x = 300
            ball.rect.y = 200
            if score_r >= 3:
                win_r.draw() 
                restart.draw() 
                finish = True

        if ball.rect.x > win_width - 50:
            score_l += 1
            text_score_l.set_text('SCORE L: '+ str(score_l), 30, text_color)
            ball.rect.x = 300
            ball.rect.y = 200            
            if score_l >= 3:             
                win_l.draw() 
                restart.draw()           
                finish = True  

    


    

        
    
