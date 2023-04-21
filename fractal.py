import numpy as np, pygame as pg,threading as t,time

full_screen=True
if not full_screen:
    width,height=(600,600)
    window=pg.display.set_mode((width,height))
else:
    window=pg.display.set_mode((0,0),pg.FULLSCREEN)
    width,height=window.get_width(),window.get_height()
    
key_press=[]
clock = pg.time.Clock()

def run(clear):
    key_press.clear()
    pg.display.update()
    if clear:window.fill((0,0,0))
    fps=(clock.tick()/1000)+0.01
    pg.display.set_caption(f"FPS --> {round(1/fps,1)}")
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            return False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                pg.quit
                return False
            if event.key==pg.K_SPACE:
                key_press.append("space")
    return True

def maper(v,mini,maxi,mino,maxo):
    return (((v-mini)/(maxi-mini))*(maxo-mino))+mino

def formulaImag(vec,c):
    return (vec**2)+c

def bound(x,y,times=16):
    # vec=complex(x,y)
    vec=complex(x,y)
    itr=0
    for i in range(times):
        vec=formulaImag(vec, complex(x,y))
        itr+=1
        if (abs(vec.real+vec.imag)>16):
            break
    return itr/times

pixel=pg.PixelArray(window)

pixels_per_thread=10
noOfcell=int(width/pixels_per_thread)

canvas=[[-2.5,1.0],
        [-1.5,1.5]]

def draw_in_bound():
    for i in range(width):
        for j in range(height):
            x=maper(i,0,width,canvas[0][0],canvas[0][1])
            y=maper(j,0,height,canvas[1][0],canvas[1][1])
            
            col=np.ones(3)*bound(x,y,100)
            pixel[i][j]=tuple((col)*255)
            
def draw_in_bound_thred(depth):
    grid=[]
    for i in range(noOfcell):
        for j in range(noOfcell):
            x=t.Thread(target=per_thred_bound,args=(i,j,pixels_per_thread,width,height,canvas,depth))
            grid.append(x)
            x.start()
    print("=====",t.activeCount(),"=====")
    for i in grid:i.join()


def per_thred_bound(i,j,pixels_per_thread,width,height,canvas,depth):
    for k in range(pixels_per_thread):
        for l in range(pixels_per_thread):
            x=maper((i*pixels_per_thread)+k,0,width,canvas[0][0],canvas[0][1])
            y=maper((j*pixels_per_thread)+l,0,height,canvas[1][0],canvas[1][1])
            col=bound(x,y,5**depth)*255
            pixel[(i*pixels_per_thread)+k][(j*pixels_per_thread)+l]=(col,col,col)


t1=time.time()
draw_in_bound()
depth=2
# draw_in_bound_thred(depth)
print(round(time.time()-t1,2),"sec")
while run(False):
    if pg.mouse.get_pressed()[0]==1:
        s_x,s_y=pg.mouse.get_pos()
        while run(False):
            n_x,n_y=pg.mouse.get_pos()
            pg.draw.rect(window,(0,100,10),[s_x,s_y,n_x-s_x,n_y-s_y])
            if pg.mouse.get_pressed()[0]==0:
                canvas1=[[maper(s_x,0,width,canvas[0][0],canvas[0][1]),
                          maper(n_x,0,width,canvas[0][0],canvas[0][1])],
                         [maper(s_y,0,height,canvas[1][0],canvas[1][1]),
                          maper(n_y,0,height,canvas[1][0],canvas[1][1])]]
                canvas=canvas1
                depth+=1
                break
        draw_in_bound()
        # draw_in_bound_thred(depth)