import pygame as pg
from math import sin,cos
print("use key 0,1,2,3 for intrensic circle and x-axis for radi and y for turn")
width,height=400,400
window=pg.display.set_mode((width,height))
def update():
    pg.display.update()
    window.fill((0,0,0))
    for event in pg.event.get():
        if event.type ==pg.QUIT:quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_0:return 4
            if event.key == pg.K_1:return 1
            if event.key == pg.K_2:return 2
            if event.key == pg.K_3:return 3
    return None
s = lambda r,c,t:r*sin(t*c)
c = lambda r,c,t:r*cos(t*c)
def pos(t,r1,c1,r2,c2,r3,c3):
    x=s(r1,c1,t)+s(r2,c2,t)+s(r3,c3,t)
    y=c(r1,c1,t)+c(r2,c2,t)+c(r3,c3,t)
    return (x+width/2,y+height/2)
maper = lambda Var,MinIn,MaxIn,MinOut,MaxOut:(((Var-MinIn)/(MaxIn-MinIn))*(MaxOut-MinOut))+MinOut
mode=4
r1=c1=r2=c2=r3=c3=1
length=100
while 1:
    key=update()
    q,w=pg.mouse.get_pos()
    if key:mode=key
    if mode==4:length,p=maper(q,0,width,10,1000),maper(w,0,height,-3,3)
    elif mode==1:r1,c1=maper(q,0,width,0,200),maper(w,0,height,-3,3)
    elif mode==2:r2,c2=maper(q,0,width,0,200),maper(w,0,height,-3,3)
    elif mode==3:r3,c3=maper(q,0,width,0,200),maper(w,0,height,-3,3)
    p_0=None
    for t in range(int(length)):
        p_0=(pos(t/10,r1,c1,r2,c2,r3,c3))
        p_1=(pos((t+1)/10,r1,c1,r2,c2,r3,c3))
        pg.draw.line(window,(0,255,0),p_0,p_1)




    

