import pygame as pg
import random
from math import *
init = pg.init()
width = 600
height = 600
window = pg.display.set_mode((width, height))
pg.display.set_caption('my_game')
# colors...
C_BWRGBYCM = [(0,0,0),(255, 255, 255),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(0, 255, 255),(255, 0, 255)]

# game_variables...
exit_game = False
clock = pg.time.Clock()
fps = 40
zero = (width/2, height/2)
a1_v = 0
a2_v = 0
G = 1 #gravitasnal constant...
m1 = 100 #mass of the first bol
m2 = 100 #mass of the second bol
r1 = 100 # length of the first thread
r2 = 80 #length of the second thread
a1 = random.randint(0,360) #angle of first bol
a2 = random.randint(0,360) # angle of second bol
fric = 0.001 # power of friction...
# function...
circles = []
def cir(v):
        pg.draw.circle(window, C_BWRGBYCM[1], (int(v[1]),int(v[0])), 7, 0)
def cir2(v):
        pg.draw.circle(window, C_BWRGBYCM[2], (int(v[0]),int(v[1])), 1, 0)
def line(a,b):
    pg.draw.line(window, C_BWRGBYCM[3], a, b, 2)
# game main loop...
while not exit_game:
    # q,w = pag.position()
    # r1 = q/8 
    # r2 = w/8
    window.fill(C_BWRGBYCM[0])
    for event in pg.event.get():
        if event.type==pg.QUIT:
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                loop()
            if event.key == pg.K_ESCAPE:
                quit()
# enter your code hear...
    # proccesing...
    num1 = (-G*(2*m1+m2))*sin((a1))
    num2 = -m2*G*sin((a1-2*a2))
    num3 = -2*sin((a1-a2)*m2)
    num4 = (a2_v**2)*r2+(a1_v**2)*r1*cos((a1-a2))
    den = r1*(2*m1+m2-m2*cos((2*a1-2*a2)))
    
    a1_ac = ((num1 + num2 +num3*num4)/den)*1
    
    num1 = 2*sin((a1-a2))
    num2 = ((a1_v**2)*r1*(m1+m2))
    num3 = G * (m1 + m2) * cos((a1))
    num4 = (a2_v**2)*r2*m2*cos((a1-a2))
    den = r2*(2*m1+m2-m2*cos((2*a1-2*a2)))
    a2_ac = ((num1*(num2+num3+num4))/den)*1
    
    x1 = (r1 * sin((a1)))+width/2
    y1 = (r1 * cos((a1)))+height/2
    
    x2 = x1+(r2 * sin((a2)))
    y2 = y1+(r2 * cos((a2)))
    # drawing...
    cir(zero)
    line(zero,(int(x1),int(y1)))
    cir((y1,x1))
    line((int(x1),int(y1)),(int(x2),int(y2)))
    cir((y2,x2))
    circles.append((x2,y2))
    for i in range(len(circles)):
        if i != 0:
            line(circles[i],circles[i-1])
            # cir2(circles[i])
    pg.display.update()
    clock.tick(fps)
    a1_v += a1_ac
    a2_v += a2_ac
    a1 += a1_v
    a2 += a2_v

    a1_v *= 0.995
    a2_v *= 0.995
# end_of_the_code...
pg.quit()
quit()
