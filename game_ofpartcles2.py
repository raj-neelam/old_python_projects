import pygame as pg
from random import *
from pygame.constants import  K_RETURN, K_b, K_c, K_e, K_f, K_g, K_i, K_m, K_n, K_r, K_t, K_w, K_y
val = [[randint(-6000,6000) for i in range(7)] for i in range(7)]
width,height=600,600
window=pg.display.set_mode((width,height))
cir=lambda pos,color,radii:pg.draw.circle(window,C_BWRGBYCM[color],(int(pos[0]),int(pos[1])),radii,0)
dis=lambda a,b:(((b[0]-a[0])**2)+((b[1]-a[1])**2))**0.5
force=lambda a,b,ar:ar/dis(a,b)**2
C_BWRGBYCM=[(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255)]
clock=pg.time.Clock()
fps=400
t=fric=tracing=infinite_space=exit_game=0
friction=0.9
radius=3
circles=[]
def make_circles_at_mouse(k):
    point=pg.mouse.get_pos()
    circles.append([[point[0],point[1]],k,0,0])
def add_particles():    circles.append([[randint(0+radius,width-radius),randint(0+radius,height-radius)],randint(1,7),randint(-t,t),randint(-t,t)])
while 1:
    if tracing%2==0:    window.fill(C_BWRGBYCM[0])
    for event in pg.event.get():
        if event.type==pg.QUIT: quit()
        if event.type==pg.KEYDOWN:
            if event.key==K_n:    circles=[]
            if event.key==K_RETURN:   val=[[randint(-6000,6000) for i in range(7)] for i in range(7)]
            if event.key==K_i:    infinite_space+=1
            if event.key==K_f:    fric+=1
            if event.key==K_t:    tracing+=1
            if event.key==K_e:    val=[[0,0,0,0,0,0,0],[0,6000,0,0,0,-6000,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,-6000,0,0,0,6000,0],[0,0,0,0,0,0,0]]
            if event.key==K_w:    make_circles_at_mouse(1)
            if event.key==K_r:    make_circles_at_mouse(2)
            if event.key==K_g:    make_circles_at_mouse(3)
            if event.key==K_b:    make_circles_at_mouse(4)
            if event.key==K_y:    make_circles_at_mouse(5)
            if event.key==K_c:    make_circles_at_mouse(6)
            if event.key==K_m:    make_circles_at_mouse(7)
            if event.key==pg.K_SPACE:
                for i in range(20): add_particles()
            if event.key==pg.K_ESCAPE:    quit()
    for no,circle in enumerate(circles):
        for no_2,all_cir in enumerate(circles):
            if circle[0][0]!=all_cir[0][0] and circle[0][1]!=all_cir[0][1]:
                xl,yl=circle[1]-1,all_cir[1]-1
                forceb=force(circle[0],all_cir[0],val[xl][yl])  
                if circle[0][0]-all_cir[0][0]>0:    circle[2]+=forceb
                if circle[0][0]-all_cir[0][0]<0:    circle[2]-=forceb
                if circle[0][1]-all_cir[0][1]>0:    circle[3]+=forceb
                if circle[0][1]-all_cir[0][1]<0:    circle[3]-=forceb
                if dis(circle[0],all_cir[0])<=2*radius+1:   circle[3],all_cir[3],circle[2],all_cir[2]=0,0,0,0
        if fric%2==0:   circle[2],circle[3]=circle[2]*friction,circle[3]*friction
        circle[0][0]+=circle[2]/100
        circle[0][1]+=circle[3]/100
        cir(circle[0],circle[1],radius)
        if infinite_space%2==0:
            if circle[0][0]-radius<0:   circle[2],circle[0][0]=-circle[2],circle[0][0]+1
            elif circle[0][0]+radius>width: circle[2],circle[0][0]=-circle[2],circle[0][0]-1
            elif circle[0][1]-radius<0: circle[3],circle[0][1]=-circle[3],circle[0][1]+1
            elif circle[0][1]+radius>height:    circle[3],circle[0][1]=-circle[3],circle[0][1]-1
        else:
            if circle[0][0]<0:  circle[0][0]=width
            elif circle[0][0]>width:  circle[0][0]=0
            elif circle[0][1]<0:  circle[0][1]=height
            elif circle[0][1]>height: circle[0][1]=0
    pg.display.update()
    clock.tick(fps)
