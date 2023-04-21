import pygame as pg
import numpy as np
from random import *
width,height,C_BWRGBYCM=80,80,((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
window=pg.display.set_mode((width, height))
maper = lambda vari,minV,maxV,minO,maxO:(vari-minV)/(maxV-minV)*(maxO-minO)+minO
def event_check():
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
def shift(a):
	if a==0:return choice([3,0,1])
	elif a==1:return choice([0,1,2])
	elif a==2:return choice([1,2,4])
	elif a==3:return choice([0,3,5])
	elif a==4:return choice([2,4,7])
	elif a==5:return choice([3,5,6])
	elif a==6:return choice([5,6,7])
	elif a==7:return choice([6,7,4])
def ant_move(ant,based_on):
	x,y,p=ant
	while 1:
		c=1
		if based_on=="red":
			a=None
			strenth=-1
			if x!=0 and y!=0:
				if 0>pheramons[x-1][y-1]>=strenth:
					strenth=pheramons[x-1][y-1]
					a=0
					c=0
			if y!=0:
				if 0>pheramons[x][y-1]>=strenth:
					strenth=pheramons[x][y-1]
					a=1
					c=0
			if x!=width-1 and y!=0:
				if 0>pheramons[x+1][y-1]>=strenth:
					strenth=pheramons[x+1][y-1]
					a=2
					c=0
			if x!=0:
				if 0>pheramons[x-1][y]>=strenth:
					strenth=pheramons[x-1][y]
					a=3
					c=0
			if x!=width-1:
				if 0>pheramons[x+1][y]>=strenth:
					strenth=pheramons[x+1][y]
					a=4
					c=0
			if x!=0 and y!=height-1:
				if 0>pheramons[x-1][y+1]>=strenth:
					strenth=pheramons[x-1][y+1]
					a=5
					c=0
			if y!=height-1:
				if 0>pheramons[x][y+1]>=strenth:
					strenth=pheramons[x][y+1]
					a=6
					c=0
			if x!=width-1 and y!=height-1:
				if 0>pheramons[x+1][y+1]>=strenth:
					strenth=pheramons[x+1][y+1]
					a=7
					c=0
			if c==1:strenth=0
		# 	########################
		elif based_on=="blue":
			a=None
			strenth=1
			if x!=0 and y!=0:
				if 0<pheramons[x-1][y-1]<=strenth:
					strenth=pheramons[x-1][y-1]
					a=0
					c=0
			if y!=0:
				if 0<pheramons[x][y-1]<=strenth:
					strenth=pheramons[x][y-1]
					a=1
					c=0
			if x!=width-1 and y!=0:
				if 0<pheramons[x+1][y-1]<=strenth:
					strenth=pheramons[x+1][y-1]
					a=2
					c=0
			if x!=0:
				if 0<pheramons[x-1][y]<=strenth:
					strenth=pheramons[x-1][y]
					a=3
					c=0
			if x!=width-1:
				if 0<pheramons[x+1][y]<=strenth:
					strenth=pheramons[x+1][y]
					a=4
					c=0
			if x!=0 and y!=height-1:
				if 0<pheramons[x-1][y+1]<=strenth:
					strenth=pheramons[x-1][y+1]
					a=5
					c=0
			if y!=height-1:
				if 0<pheramons[x][y+1]<=strenth:
					strenth=pheramons[x][y+1]
					a=6
					c=0
			if x!=width-1 and y!=height-1:
				if 0<pheramons[x+1][y+1]<=strenth:
					strenth=pheramons[x+1][y+1]
					a=7
					c=0
			if c == 1:strenth=0
		########################
		# a,strenth=0,0
		a=shift(a)
		if strenth==0:
			a = randint(0, 7)
		if a==0:
			if x == 0: continue
			elif y == 0: continue
			else: return [x-1,y-1,p]
		elif a==1:
			if y==0:continue
			else:return [x,y-1,p]
		elif a==2:
			if x == width-1:continue
			elif y==0:continue
			else:return [x+1,y-1,p]
		elif a==3:
			if x==0:continue
			else:return [x-1,y,p]
		elif a==4:
			if x==width-1:continue
			else:return [x+1,y,p]
		elif a==5:
			if x==0:continue
			elif y==height-1:continue
			else:return [x-1,y+1,p]
		elif a==6:
			if y==height-1:continue
			else:return [x,y+1,p]
		elif a==7:
			if x==width-1:continue
			elif y==height-1:continue
			else:return [x+1,y+1,p]
def filerw(file_name,content=""):
    """pass clear to clear the output"""
    if content=="":
        f = open(file_name)
        cont = f.read()
        f.close()
        return cont
    elif content=="clear":
        f = open(file_name,"w")
        f.write("")
        f.close()
        return None
    else:
        f = open(file_name,"a")
        f.write(content)
        return None
filerw('data1.txt',"clear")
pixel = pg.PixelArray(window)
pheramons = np.zeros((width,height))
foods = np.zeros((width,height))
ants = np.array([[width//2,height//2,int(i%2==0)] for i in range(1000)])
# -----ant-------x--y-----food-0/1
evaporation_amt=0.01
strin=""
while 1:
	event_check()
	# window.fill(C_BWRGBYCM[0])
	if pg.mouse.get_pressed()[0]==1:
		q,w=pg.mouse.get_pos()
		for i in range(q-5,q+5):
			for j in range(w-5,w+5):
				foods[i][j]=1
	for x in range(width):
		for y in range(height):
			if -0.01<pheramons[x][y]<0.01:pheramons[x][y]=0
			if 0<pheramons[x][y]<=1:
				pheramons[x][y]-=evaporation_amt
				pixel[x][y]=(0,0,maper(pheramons[x][y],0,1,0,255))
			elif -1<=pheramons[x][y]<0:
				pheramons[x][y]+=evaporation_amt
				pixel[x][y]=(maper(pheramons[x][y],-1,0,255,0),0,0)
			if foods[x][y]==1:
				pixel[x][y]=C_BWRGBYCM[5]
			val=pixel[x][y]
			if val == 0:strin+=","
			else:strin+=str(val)+","
	for no,ant in enumerate(ants):
		if ant[2]==0:
			ants[no] = ant_move(ant,"red")
			pheramons[ant[0]][ant[1]]=1
			if foods[ant[0]][ant[1]]==1:
				ant[2]=1
				foods[ant[0]][ant[1]]=0
		elif ant[2]==1:
			ants[no] = ant_move(ant,"blue")
			pheramons[ant[0]][ant[1]]=-1
		pixel[ant[0]][ant[1]]=C_BWRGBYCM[3]
		if width-5<ant[0]<width and height-5<ant[1]<height:ant[2]=0
	pixel[width-1][height-1]=C_BWRGBYCM[7]
	filerw("data1.txt",f"{strin}")
	strin=""


