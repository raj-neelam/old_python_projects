import pygame as pg
pg.init()
width,height = 1300, 200
window = pg.display.set_mode((width, height))
# colors...
C_BWRGBYCM = [(0,0,0),(255, 255, 255),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(0, 255, 255),(255, 0, 255)]
# game_variables...
exit_game = False
clock = pg.time.Clock()
fps = 800
mas = 0.00000001
x_b1,y_b1 = width*0.8,60
mass_b1 = mas*10000000000
x_b2,y_b2 = width*0.4,110
mass_b2 = mas
v_b2 = 0
v_b1 = 0.0001
colition = 0
u1 = u2 = 0
front = pg.font.SysFont('None',30)
# function...
def rect(pos_l_b,color):
    pg.draw.rect(window,color,(pos_l_b))
def text_screen(text, cor,color):
    texts = front.render(str("colisions = "+ text), True, color)
    window.blit(texts, (cor[0], cor[1]))
def cal(v1,v2,m1,m2):
    u1 = v1
    u2 = v2
    a1 = ((m1-m2)/(m1+m2))*u1
    a2 = (2*m2/(m1+m2))*u2
    v1 = a1+a2
    a1 = (2*m1/(m1+m2))*u1
    a2 = ((m2-m1)/m1+m2)*u2
    v2 = a1+a2
    return v1,v2
def calculation(v1,v2,m1,m2):
    u1 = v1
    u2 = v2
    sumold = (m1*u1)+(m2*u2)
    v1 = -(sumold-(m2*v2))/m1
    v2 = (sumold-(m1*v1))/m2
    return v1,v2
# game main loop...
while not exit_game:
    window.fill(C_BWRGBYCM[0])
    for event in pg.event.get():
        if event.type==pg.QUIT:
            exit_game = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                quit()
    rect((int(x_b1),int(y_b1),100,100),C_BWRGBYCM[4])
    rect((int(x_b2),int(y_b2),50,50),C_BWRGBYCM[3])
# calculations...
    for i in range(100000):
        x_b2 -= v_b2
        x_b1 -= v_b1
        if x_b2 <= width*0.2:
            v_b2 = -v_b2
            colition+=1
        if x_b2+50 >= x_b1:
            # v_b1 = -v_b1
            v_b1,v_b2 = cal(v_b1,v_b2,mass_b1,mass_b2)
            colition+=1
    text_screen(str(colition),(0,0),C_BWRGBYCM[1])
    rect((width*0.2,0,0,height),C_BWRGBYCM[2])
    rect((0,int(height*0.8),width,200),C_BWRGBYCM[7])
    pg.display.update()
    clock.tick(fps)
pg.quit()
quit()
