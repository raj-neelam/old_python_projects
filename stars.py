import pygame as pg
from random import *
import math
width,height,C_BWRGBYCM=400,400,((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
window=pg.display.set_mode((width, height))
def event_check():
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
cir = lambda pos,color,radi:pg.draw.circle(window,(color,color,color),(int(pos[0]),int(pos[1])),radi,0)
points=[]
max_vel=2
maper = lambda vari,minV,maxV,minO,maxO:(vari-minV)/(maxV-minV)*(maxO-minO)+minO
def make_point():
	points.append([randint(0,width),randint(0,height)])
for _ in range(500):make_point()
while 1:
	event_check()
	window.fill(C_BWRGBYCM[0])
	for no,point in enumerate(points):
		point[0]+=maper(point[0],0,width,-1,1)
		point[1]+=maper(point[1],0,height,-1,1)
		cir((point[0],point[1]),int(maper(math.dist((width//2,height//2),(point[0],point[1])),0,289,50,255)),1)
		if point[0]<0 or point[0]>width or point[1]<0 or point[1]>height:
			points.pop(no)
			make_point()