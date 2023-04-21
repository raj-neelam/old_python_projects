import pygame as pg
from random import *
width,height,C_BWRGBYCM=100,100,((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
window=pg.display.set_mode((width, height))
col = lambda a:C_BWRGBYCM[4] if(a==1) else C_BWRGBYCM[0]
def event_check():
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
pixel=pg.PixelArray(window)
live_deth2=[[0 for i in range(0,height)] for j in range(0,width)]
live_deth=[[0 for i in range(0,height)] for j in range(0,width)]
times=1
for i in range(2,99):
	for j in range(2,3):
		live_deth[i][j]=1
for i in range(2,99):
	for j in range(98,99):
		live_deth[i][j]=1
while 1:
	event_check()
	window.fill(C_BWRGBYCM[0])
	for x in range(1,width-1):
		for y in range(1,height-1):
			try:pixel[x][y]=col(live_deth[x][y])
			except:pass
	for x in range(1,width-1):
		for y in range(1,height-1):
			neighbours=0
			try:
				neighbours+=live_deth[x-1][y]
				neighbours+=live_deth[x-1][y+1]
				neighbours+=live_deth[x][y+1]
				neighbours+=live_deth[x+1][y+1]
				neighbours+=live_deth[x+1][y]
				neighbours+=live_deth[x+1][y-1]
				neighbours+=live_deth[x][y-1]
				neighbours+=live_deth[x-1][y-1]
			except:pass
			if live_deth[x][y]==1:
				if neighbours<2:live_deth2[x][y]=0
				elif 1<neighbours<4:live_deth2[x][y]=1
				elif neighbours>3:live_deth2[x][y]=0
			elif live_deth[x][y]==0:
				if neighbours==3:live_deth2[x][y]=1
	live_deth=live_deth2