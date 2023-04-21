import pygame as pg
import pyautogui as pag
init = pg.init()
width = 800
height = 800
window = pg.display.set_mode((width, height))
pg.display.set_caption('my_game')
# colors...
C_BWRGBYCM = [(0,0,0),(255, 255, 255),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(0, 255, 255),(255, 0, 255)]

# game_variables...
exit_game = False
clock = pg.time.Clock()
fps = 400
zoom = 250 # aprox 100
def cir(v):
        pg.draw.circle(window, v[2], (int(v[1]),int(v[0])), 7, 0)
# game main loop...
k = 0
q = -0.835 #-0.8 #-0.70176
w = -0.2321 #0.156 #-0.4842
while not exit_game:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            exit_game = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                loop()
            if event.key == pg.K_ESCAPE:
                quit()

# enter your code hear...
    # q,w = pag.position()
    # q = (q-500)/1000
    # w = (w-350)/1000
    if q > 1 :
        q = 1
    if w > 1 :
        w = 1
    if k == 0:
        # window.fill(C_BWRGBYCM[1])
        for i in range(width+2):
            for j in range(height+2):
                n = 0
                a,b = ((i-int(width/2)-0)/zoom),(((j)-int(width/2))/zoom)
                ca,cb = a,b
                while n<50:
                    # aa = a*a - b*b
                    # bb = 2*a*b
                    # a = aa + ca
                    # b = bb + cb
                    aa = a*a
                    bb = b*b
                    twoab = 2*a*b
                    a = aa-bb+q
                    b = twoab +w
                    if abs(a + b) > 4:
                        break
                    n += 1
            
                # print(abs(a+b))
                # c = C_BWRGBYCM[0]
                c = (n*2+50,0,0)
                # if n == 100:
                #     c = C_BWRGBYCM[1]
                cir((j,i,c))
            
                k = 1
            #     j += height/100
            # i += width/100    
        # print('done')
    pg.display.update()
    clock.tick(fps)
# end_of_the_code...
pg.quit()
quit()