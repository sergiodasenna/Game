# -*- coding: utf-8 -*- 

import pygame
import random
import time

#создание игрового окна и игровой области
window = pygame.display.set_mode((400,530))
pygame.display.set_caption('Asteroid Attack')
screen = pygame.Surface((400,500))
info = pygame.Surface((400,30))
#класс объектов игры
class Sprite:
    def __init__(self, xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def render(self):
        screen.blit(self.bitmap, (self.x,self.y))
    
#шрифты
pygame.font.init()
inf_font = pygame.font.Font(None, 32)

asteroid = []
for i in range(1000):
    a = random.randint(0,4)
    asteroid.append(Sprite(10+a*80, 0, 'asteroid.png'))
        
spaceship = Sprite(170, 360, 'spaceship2.png')
boom = Sprite(170,360,'boom.png')

time0 = time.time()
t = (time.time()-time0)//1
#time.sleep(61)
#tim = time.time()-time0
#print(tim)

#time = time.time()-time0
#print(time)
    
done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
            
        if (e.type == pygame.KEYDOWN) and (spaceship != boom):
                if e.key == pygame.K_LEFT:
                    if spaceship.x > 10:
                        spaceship.x -=80
                        
                if e.key == pygame.K_RIGHT:
                    if spaceship.x < 310:
                        spaceship.x +=80
                        
            
    screen.fill((31,5,64))
    info.fill((255,255,255))
    asteroid[0].y +=0.1
    for i in range(1,1000):
        if asteroid[i-1].y>80:
            t = (time.time() - time0)//1
            asteroid[i].y +=0.2+t*0.01
        if (asteroid[i].y>310) and (asteroid[i].y<400) and (asteroid[i].x == spaceship.x):
            boom.x = spaceship.x
            boom.y = spaceship.y
            spaceship = boom
            
    for i in range(1,1000):
        if asteroid[i-1].y>70:
            asteroid[i].render()
            
    spaceship.render()
        


    info.blit(inf_font.render(str(t), 1, (0,0,0)), (10,5))
    window.blit(info,(0,0))
    window.blit(screen, (0,30))
    pygame.display.flip()