import pygame as pg
import random
from math import *
width,height = 500, 500
window = pg.display.set_mode((width, height))
# colors...
C_BWRGBYCM = [(0,0,0),(255, 255, 255),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(0, 255, 255),(255, 0, 255)]
def cir(pos,color,redii):
    pg.draw.circle(window,C_BWRGBYCM[color],(int(pos[0]),int(pos[1])),redii,0)
def line(a,b,color):
    pg.draw.line(window,C_BWRGBYCM[color],(int(a[0]),int(a[1])),(int(b[0]),int(b[1])),1)
def make_pend(lists):
    """list in order [angle,orign,color,vel,acc,xbob,ybob]"""
    for no,lis in enumerate(lists):
        color = lis[2]
        lis[5] = (sin(lis[0])*lenth)+lis[1][0]
        lis[6] = (cos(lis[0])*lenth)+lis[1][1]
        line(lis[1],(lis[5],lis[6]),color-1)
        cir((lis[5],lis[6]),color,10)
        lis[4]=(sin(lis[0])*-0.0001)
        lis[3]+= lis[4]+0.0000000099
        lis[0]+=lis[3]
# game_variables...
exit_game = False
clock = pg.time.Clock()
fps = 400
lenth = 200
mass = 100
gravity = 0
listes = []
for i in range(100):
    listes.append([random.randint(0,600)/100,(width/2,height/2),random.randint(2,7),0,0,0,0])
# game main loop...
while not exit_game:
    window.fill(C_BWRGBYCM[0])
    for event in pg.event.get():
        if event.type==pg.QUIT:
            exit_game = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                quit()
# enter your code hear...
    
    make_pend(listes)
    # print(liste)
    pg.display.update()
    clock.tick(fps)
# end_of_the_code...
pg.quit()
quit()
