import pygame as pg
import numpy as np
width,height=600,600
fw,fh=30,30
window = pg.display.set_mode((width,height))
sidew,sideh=width/fw,height/fh
cloak = pg.time.Clock()
fps=0
drain=0.1
intencity=1.01
screen = np.zeros((fw,fh))
def update():
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
def update_screen():
    for y in range(fw):
        for x in range(fh):
            c=int(screen[x][y])
            pg.draw.rect(window,(c,c,c),
                         [x*sidew,y*sideh,sidew,sideh])
def mouse_sen():
    if pg.mouse.get_pressed()[0]==1:
        pos=pg.mouse.get_pos()
        x = int(pos[0]//sidew)
        y = int(pos[1]//sideh)
        screen[x][y]=255
def blur():
    for y in range(1,fw-1):
        for x in range(1,fh-1):
            c=0
            for i in range(-1,2):
                for j in range(-1,2):
                    c+=screen[x+i][y+j]
            c=c/9
            screen[x][y]=clip(c*intencity)
            screen[x][y]=clip(screen[x][y]-drain)
def clip(v):
    if v>255:return 255
    if v<0:return 0
    return v
while update():
    mouse_sen()
    blur()
    update_screen()
    pass
