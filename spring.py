import pygame as pg
from time import time
width,height=400,400
window = pg.display.set_mode((width,height))
clock=pg.time.Clock()
fps=50
def update():
    clock.tick(fps)
    pg.display.update()
    window.fill((0,0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            return False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                pg.quit()
                return False
    return True
class Body:
    def __init__(self,pos,A,mean_pos):
        self.pos=pos
        self.vel=0
        self.mean_pos=mean_pos
        self.A=A
        self.k=0.7
        self.mass=100
        self.W=(self.k/self.mass)**0.5
    def move(self,dt):
        #self.vel=self.W*((self.A**2)-((self.pos-self.mean_pos)**2))**0.5
        self.vel+=(self.mean_pos-self.pos)*(self.W**2)*dt
        self.pos+=self.vel
    def draw(self):
        pg.draw.circle(window,(0,255,0),(self.pos,height/2),10)

        pg.draw.line(window,(255,255,255),(self.mean_pos,0),(self.mean_pos,height))
        pg.draw.line(window,(255,0,0),(self.mean_pos+self.A,0),(self.mean_pos+self.A,height))
        pg.draw.line(window,(255,0,0),(self.mean_pos-self.A,0),(self.mean_pos-self.A,height))
body=Body(300,100,200)
t1=time()
while update():
    dt=time()-t1
    t1=time()
    body.move(dt)
    body.draw()
pg.quit()
'''
 F=-kx
 a=-kx/m
 a=w^2x   :- sqrt(k/m)
 v=w(A^2-X^2)^0.5
'''



















