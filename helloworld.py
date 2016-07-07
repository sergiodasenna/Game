# -*- coding: utf-8 -*- 

import pygame
import random
import time
import sys
import os

#создание игрового окна и игровой области
window = pygame.display.set_mode((400,530))
pygame.display.set_caption('Asteroid Attack')
screen = pygame.Surface((400,500))
info = pygame.Surface((400,30))
menu = pygame.Surface((400, 200))

#чтение рекорда
f = open('record.txt', 'r')
record = int(f.read())

#класс объектов игры
class Sprite:
    def __init__(self, xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def render(self):
        screen.blit(self.bitmap, (self.x,self.y))

#функция рестарта        
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
#шрифты
pygame.font.init()
inf_font = pygame.font.Font(None, 32)
go_font = pygame.font.Font(None, 64)
message_font = pygame.font.Font(None, 32)
record_font = pygame.font.Font(None, 32)

#объявление переменных
asteroid = []
for i in range(1000):
    a = random.randint(0,4)
    asteroid.append(Sprite(10+a*80, 0, 'asteroid.png'))
        
spaceship = Sprite(170, 360, 'spaceship2.png')
boom = Sprite(170,360,'boom.png')

#время
time0 = time.time()
t = int(time.time()-time0)
if (spaceship != boom):
    score = t
#цикл программы
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
        if (spaceship == boom) and (e.type == pygame.KEYDOWN):
            restart_program()
                        
            
    screen.fill((31,5,64))
    info.fill((31,85,160))
    menu.fill((34,53,149))
    
    asteroid[0].y +=0.1
    for i in range(1,1000):
        
        if asteroid[i-1].y>130:
            t = int(time.time() - time0)
            if (spaceship != boom):
                score = t
            if (score>record) and (spaceship != boom):
                record = score
                #запись рекорда
                f = open('record.txt', 'w')
                f.write(str(record))
                f.close()
            asteroid[i].y +=0.3+t*0.01
            
        if (asteroid[i].y>310) and (asteroid[i].y<400) and (asteroid[i].x == spaceship.x):
            boom.x = spaceship.x
            boom.y = spaceship.y
            spaceship = boom
    #отрисовка объектов
    for i in range(1,1000):
        if asteroid[i-1].y>130:
            asteroid[i].render()
            
    spaceship.render()
        

    #отрисовка шрифтов
    if (spaceship == boom):
        menu.blit(go_font.render('GAME OVER', 1, (173,161,23)), (70,70))
        menu.blit(message_font.render('Press any key to try again', 1, (173,161,10)), (68,120))
                
    info.blit(inf_font.render('Score: ' + str(score), 1, (0,0,0)), (10,5))
    info.blit(record_font.render('Record: ' + str(record),1,(0,0,0)), (250,5))
    #отрисовка слоёв
    window.blit(info,(0,0))
    window.blit(screen, (0,30))
    if (spaceship == boom):  
        window.blit(menu, (0,165))

    pygame.display.flip()
