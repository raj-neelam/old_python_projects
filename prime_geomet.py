import pygame as pg
import random
from math import *
width,height = 710,710
window = pg.display.set_mode((width, height))
pg.display.set_caption('my_game')
# colors...
C_BWRGBYCM = [(0,0,0),(255, 255, 255),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(0, 255, 255),(255, 0, 255)]
def is_prime(n):
    z = int(n**0.5)
    if n == 1:
        return False
    if n == 2:
        return True
    if n>2 and n%2==0:
        return False
    for i in range(2,z+1):
        if n%i == 0:
            return False
    return True
def prime_lis(n):
    l = []
    for i in range(1,n+1):
        if is_prime(i):
            l.append(i)
    return l
def cir(v,c,s):
    pg.draw.circle(window, (C_BWRGBYCM[c]) , v, s, 0)
def cir2(v,c,s):
    for i in v:
        pg.draw.circle(window, (C_BWRGBYCM[c]) , i, s, 0)
def val(a1,lengt):
    v1 = (cos(a1+((pi/2)+pi))*lengt)+width/2
    v2 = (sin(a1+((pi/2)+pi))*lengt)+height/2
    return (int(v1),int(v2))
def line(a,b):
    pg.draw.line(window, C_BWRGBYCM[3], a, b, 2)
# game_variables...
exit_game = False
game_over = False
clock = pg.time.Clock()
fps = 1000
length = 1
lis_s = []
angle = 0
prim = prime_lis(1000000)
#game main loop...
# /////////////////////////////////////prime
while not exit_game:
    
    # print(prim)
    for p in range(len(prim)):
        for event in pg.event.get():
            if event.type==pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quit()

#     # enter your code hear...
        point = val(prim[p],length)
        lis_s.append(point)
        cir2(lis_s,3,1)
        # angle+=1
        length+=0.04
        pg.display.update()
        clock.tick(fps)
    

# /////////////////////////////whole
'''
while not exit_game:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                quit()

    # enter your code hear...
    point = val(angle,length)
    lis_s.append(point)
    cir2(lis_s,3,1)
    # for i in range(len(lis_s)):
    #     if i != 0:
    #         line(lis_s[i],lis_s[i-1])
    # angle+=1.61803398874989
    # angle+=random.randint(4,4)
    angle+=3.448598
    length+=0.09
    # length+=1
    pg.display.update()
    clock.tick(fps)
    '''
pg.quit()
quit()
