import pygame as pg
import random
init = pg.init()
fco = random.randint(0,225)
width = 765
height = 730
window = pg.display.set_mode((width, height))
pg.display.set_caption('my_game')
# colors...
C_BWRGBYCM = [(0,0,0),(255, 255, 255),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(0, 255, 255),(255, 0, 255)]
dis = lambda a,b:(((a[0]-b[0])**2)((a[1]-b[1])**2))**0.5
def cent(a,b):
    x1,y1 = a
    x2,y2 = b
    x = (x2/2+x1/2)
    y = (y2/2+y1/2)
    return (int(x),int(y))
def randompoint():
    q = random.randint(0,width)
    w = random.randint(0,height)
    return (q,w)
# def dice():
#     return random.randint(1,6)
def cir(v):
    for va in v:
        pg.draw.circle(window, C_BWRGBYCM[2], va, 1, 0)
def cir2(v):
    pg.draw.circle(window, (int((v[0])/3),int((v[1])/3),fco), v, 1, 1)
    #pg.draw.circle(window, C_BWRGBYCM[3], v, 1, 1)
# game_variables...
exit_game = False
game_over = False
clock = pg.time.Clock()
fps = 40
# initial = []
initial = [(int(width/2),int(0)),(0,height),(int(width),height) ]
# initial = [(0,0),(int(width),int(0)),(0,height),(int(width),height) ]
points = []
# while not game_over:
#     for event in pg.event.get():    (int(width-10),int(10)),
#         x = pg.mouse.get_pressed()[0]
#         if x == 1:
#             initial.append(pg.mouse.get_pos())
#         if len(initial) == 5:
#             game_over = True
start = randompoint()
for i in range(1000000):
    no = random.randint(1,3)
    if no == 1:
        npoint = cent(start,initial[0])
    if no == 2:
        npoint = cent(start,initial[1])
    if no == 3:
        npoint = cent(start,initial[2])
    if no == 4:
        npoint = cent(start,initial[3])
    # if no == 5:
    #     npoint = cent(start,initial[4])
    start = npoint
    points.append(npoint)
# cir2(initial)
# game main loop...
k = 0
while not exit_game:
    # window.fill(C_BWRGBYCM[0])
    for event in pg.event.get():
        if event.type==pg.QUIT:
            exit_game = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                loop()
            if event.key == pg.K_ESCAPE:
                quit()
# enter your code hear...
    if k == 0:
        for i in points:
            cir2(i)
        print("done...")
        # print(points)
        k = 1
    pg.display.update()
    clock.tick(fps)

# end_of_the_code...
pg.quit()
quit()
