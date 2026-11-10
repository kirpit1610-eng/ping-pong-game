import pygame
pygame.init()
from pygame import *
from random import *
import random


class GameSprite(sprite.Sprite):
    def __init__(self, pic, x, y, scalex, scaley):
        super().__init__()
        self.image = transform.scale(image.load(pic), (scalex, scaley))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def blitning(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Area():
    def __init__(self, x, y, width, height, color = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fillcolor = (255, 255, 255)
    def fill(self):
        pygame.draw.rect(win, self.fillcolor, self.rect)
    def color(self, new_color):
        self.fillcolor = new_color
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)   

class Textwrite(Area):
    def set_text(self, text, length_text, color_text):
            self.image = pygame.font.Font(None, length_text).render(text, True, color_text)
    def draw(self, x, y):
        win.blit(self.image, (self.rect.x + x, self.rect.y + y))    
 
 
class Player(GameSprite):
    def __init__(self, pic, x, y, scalex, scaley):
        super().__init__(pic, x, y, scalex, scaley)
    def goUP(self):
        if self.rect.y > 0:
            self.rect.y -= 5
    def goDOWN(self):
        if self.rect.y < 425:
            self.rect.y += 5    
class Ball(GameSprite):
    finish = False
    def __init__(self, pic, x, y, scalex, scaley):
        super().__init__(pic, x, y, scalex, scaley)
        self.speedx = 2
        self.speedy = 3


        print(self.speedx)
        print(self.speedy)
        print('--------------')

    def movement(self):
        self.rect.x -= self.speedx
        self.rect.y -= self.speedy
        if self.colliderect(player1):
            self.speedx = randint(2,8)
            self.speedy = randint(1,4)
            if self.speedx < 0:
                self.speedx += self.speedx * 2
            else:
                self.speedx -= self.speedx * 2
            self.speedy -= self.speedy * 2
            print(ball.speedx)
            print(ball.speedy)
        elif self.colliderect(player2):
            self.speedx = -(randint(2,8))
            self.speedy = -(randint(1,4))
            if self.speedx < 0:
                self.speedx -= self.speedx * 2
            else:
                self.speedx += self.speedx * 2
            self.speedy -= self.speedy * 2
            print(ball.speedx)
            print(ball.speedy)
        if self.colliderect(wall1.rect) or self.colliderect(wall2.rect):
            self.speedy -= self.speedy *2

    def check(self):
        if self.rect.x > 730:
            Ball.finish = True
            lose.set_text('Игрок 2 проиграл!', 40, (255, 255, 255))
        if self.rect.x < -30:
            Ball.finish = True
            lose.set_text('Игрок 1 проиграл!', 40, (255, 255, 255))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)  


win = display.set_mode((700, 500))
display.set_caption('Пинг понг')
game = True
FPS = 60
clock =  time.Clock()

background = transform.scale(image.load('background.jpg'), (700, 500))

player1 = Player("racket.png",5, 210, 30, 85)
player2 = Player("racket.png",665, 210, 30, 85)

wall1 = Area(0, 490, 700, 10, (0,0,0))
wall2 = Area(0, 0, 700, 10, (0,0,0))


ball = Ball('tenis_ball.png', 350, 250, 15, 15)

lose = Textwrite(250, 250, 350, 300, None)

while game == True:
    pressedkey = key.get_pressed()
    mcl = mouse.get_pressed(3)
    mpos = mouse.get_pos()
    for e in pygame.event.get():
        if e.type == QUIT:
            game = False
    if Ball.finish == False:
        win.blit(background, (0,0))
        player1.blitning()
        player2.blitning()
        ball.blitning()
        ball.movement()
        ball.check()
        wall1.fill()
        wall2.fill()

        if pressedkey[K_w]:
            player1.goUP()
        if pressedkey[K_s]:
            player1.goDOWN()
        if pressedkey[K_UP]:
            player2.goUP()
        if pressedkey[K_DOWN]:
            player2.goDOWN()

    if Ball.finish == True:
        lose.draw(0,0)
        if mcl == (True, False, False):
            Ball.kill(ball)
            Player.kill(player1)
            Player.kill(player2)
            player1 = Player("racket.png",5, 210, 30, 85)
            player2 = Player("racket.png",665, 210, 30, 85)
            ball = Ball('tenis_ball.png', 350, 250, 15, 15)
            Ball.finish = False
            

    clock.tick(FPS)
    display.update()