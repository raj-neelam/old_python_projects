import pygame as pg
from time import time
import numpy as np
from random import uniform,randint
width,height=400,400
window = pg.display.set_mode((width,height))
clock=pg.time.Clock()
fps=50
scale=5
def update():
    clock.tick(fps)
    pg.display.update()
    #window.fill((0,0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            return False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                pg.quit()
                return False
    return True
trans=np.array([width/2,height/2])
r=lambda x:[uniform(1-x,1+x) for i in range(3)]
def col_gradi():
    return (0,0,0)
class Body:
    deviate=0.01
    def __init__(self):
        self.pos=np.ones(3)
        self.npos=np.array(r(Body.deviate))
        self.col=[randint(50,255) for i in range(3)]

        self.a=10
        self.b=28
        self.c=8/3
    def move(self,dt):
        #self.col=col_gradi()
        self.pos=self.npos.copy()
        dx=(self.a*(self.pos[1]-self.pos[0]))*dt
        dy=(self.pos[0]*(self.b-self.pos[2]))*dt
        dz=(self.pos[0]*self.pos[1]-self.c*self.pos[2])*dt
        
        self.npos[0]+=dx+dt
        self.npos[1]+=dy+dt
        self.npos[2]+=dz+dt
    def draw(self):
        a=self.pos[:2]*scale
        b=self.npos[:2]*scale
        
        #x=int(self.pos[0]+width/2)*0.5
        #y=int(self.pos[1]+width/2)*0.5
        #z=int(self.pos[2]+width/2)*0.5
        pg.draw.line(window,self.col,(a+trans),(b+trans))
t1=time()
bodys=[Body() for i in  range(400)]
while update():
    dt=time()-t1
    t1=time()
    for body in bodys:
        body.move(dt)
        body.draw()
pg.quit()
