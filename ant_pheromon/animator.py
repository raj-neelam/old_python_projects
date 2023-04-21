import pygame as pg
import numpy as np
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
data=filerw("data1.txt")
data=data.split(',')
ind=0
width,height,C_BWRGBYCM=80,80,((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
window=pg.display.set_mode((width, height))
def event_check():
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
pixel = pg.PixelArray(window)
while 1:
    event_check()
    for i in range(width):
        for j in range(height):
            try:
                a = int(data[ind])
                # print(a)
                pixel[i][j]=a
            except:pass
            ind+=1