import pygame as pg
width,height,C_BWRGBYCM=200,200,((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
window=pg.display.set_mode((width, height))
def event_check():
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
pixel=pg.PixelArray(window)
num_sand=[[0 for j in range(0,height)] for i in range(0,width)]
num_sand2=[[0 for j in range(0,height)] for i in range(0,width)]
num_sand[width//2][height//2]=10000000
while 1:
	event_check()
	window.fill(C_BWRGBYCM[0])
	for x in range(0,width):
		for y in range(0,height):
			if num_sand[x][y]==0:pixel[x][y]=C_BWRGBYCM[0]
			elif num_sand[x][y]==1:pixel[x][y]=C_BWRGBYCM[7]
			elif num_sand[x][y]==2:pixel[x][y]=C_BWRGBYCM[2]
			elif num_sand[x][y]==3:pixel[x][y]=C_BWRGBYCM[3]
			elif num_sand[x][y]>3:pixel[x][y]=C_BWRGBYCM[4]
	for times_per_frame in range(100):	
		for x in range(0,width):
			for y in range(0,height):
				if num_sand[x][y]>3:
					num_sand2[x][y]=num_sand[x][y]-4
					try:
						num_sand2[x][y-1]+=1
						num_sand2[x-1][y]+=1
						num_sand[x+1][y]+=1
						num_sand[x][y+1]+=1
					except:pass
				else:
					num_sand2[x][y]=num_sand[x][y]
		num_sand=num_sand2

