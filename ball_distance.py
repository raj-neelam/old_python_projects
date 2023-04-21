import pygame as pg,numpy as np,threading
from random import uniform
full_screen=False
if not full_screen:
    width,height=(600,600)
    window=pg.display.set_mode((width,height))
else:
    window=pg.display.set_mode((0,0),pg.FULLSCREEN)
    width,height=window.get_width(),window.get_height()
clock = pg.time.Clock()
dist = lambda x,y:((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
normal = lambda a:a/dist(a,np.zeros(2))+0.001
sub_steps=1
g=0
ball_size=(12,25)
key_press=[]
bands=3
ballsToCreatOnClick=4
num_of_thread=10

def clamp(col):
    m=max(col)
    return (col/m)*255

class Ball:
    def __init__(self,pos):
        x,y=pos
        self.pos=np.array(pos,dtype="float64")+np.array([uniform(-1,1),uniform(-1,1)])
        self.vel=np.zeros(2)
        self.raddi=uniform(ball_size[0],ball_size[1])
        self.col=np.array([(width-x)/width,y/height,(x*y)/(width*height)])*255
    def move(self,vec=np.zeros(2)):
        if self.raddi<self.pos[0]<width-self.raddi:
            if self.raddi<self.pos[1]<height-self.raddi:
                self.pos+=vec+self.vel
                self.vel+=np.array([0,g])
            else:self.wall_check(1,height)
        else:self.wall_check(0,width)
    def wall_check(self,a,horvert):
        if self.raddi>self.pos[a]:self.pos[a]=self.raddi+1
        elif horvert-self.raddi<self.pos[a]:
            self.pos[a]=horvert-self.raddi-1
            if horvert==height:
                self.vel=np.zeros(2)
        self.vel=np.zeros(2)
    def draw(self):
        # pg.draw.circle(window,self.col,self.pos,self.raddi)
        ###############################################################
        d=self.raddi/bands
        for i in range(bands):
           pg.draw.circle(window,np.full(3,255)-(self.col*(1-(i/bands))),self.pos,d*(bands-i))
        #    pg.draw.circle(window,(self.col*(1-(i/bands))),self.pos,d*(bands-i))
        

def run():
    key_press.clear()
    pg.display.update()
    window.fill((0,0,0))
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

class Grid:
    def __init__(self,x,y):
        self.cells=x,y
        self.sides=width/x,height/x
        self.col=np.array([0.5,0.8,0.5])*255
        self.lis=[[[] for j in range(y)] for i in range(x)]
        self.side_thread_x=int(x//num_of_thread)
        self.side_thread_y=int(y//num_of_thread)
    def loop_screen(self):
        if "space" in key_press:self.lis=[[[] for j in range(self.cells[1])] for i in range(self.cells[0])]
        else:
            for x in range(self.cells[0]):
                for y in range(self.cells[1]):
                    # pg.draw.rect(window,(0,100,0),[x*self.sides[0],y*self.sides[1],self.sides[0],self.sides[1]])
                    for i in range(sub_steps):self.cell_nebour_dynamics(x,y)
    def thread_loop_screen(self):
        if "space" in key_press:self.lis=[[[] for j in range(self.cells[1])] for i in range(self.cells[0])]
        else:
            thread_lis=[[None for j in range(num_of_thread)] for i in range(num_of_thread)]
            for i in range(num_of_thread):
                for j in range(num_of_thread):
                    thread_lis[i][j]=threading.Thread(target=self.thread_cell_nebour_dynamics,args=(i,j,self.side_thread_x,self.side_thread_y))
                    print(threading.activeCount())
                    thread_lis[i][j].start()
            for i in range(num_of_thread):
                for j in range(num_of_thread):
                    thread_lis[i][j].join()
    def thread_cell_nebour_dynamics(self,i,j,thread_size_x,thread_size_y):
        for x in range(thread_size_x):
            for y in range(thread_size_y):
                for i in range(sub_steps):self.cell_nebour_dynamics((i*thread_size_x)+x, (j*thread_size_y)+y)
    def cell_nebour_dynamics(self,x,y):
        if self.lis[x][y]!=[]:
            for ball in self.lis[x][y]:
                for i in range(-1,2):
                    if not -1<x+i<self.cells[0]:continue
                    for j in range(-1,2):
                        if not -1<y+j<self.cells[1]:continue
                        for item in self.lis[x+i][y+j]:
                            if item==ball:continue
                            minDis=ball.raddi+item.raddi
                            Dis=dist(ball.pos,item.pos)
                            diff=minDis-Dis
                            if diff>0:
                                self.reppel(ball,item,diff/2)
                            
                                index = self.indexOf(item)
                                if not index==item.index:
                                    self.lis[x+i][y+j].remove(item)
                                    self.addBallToLis(item)
            index = self.indexOf(ball)
            if not index==ball.index:                    
                self.lis[x][y].remove(ball)
                self.addBallToLis(ball)
    def reppel(self,b1,b2,diff):
        vec = normal(b2.pos-b1.pos)*diff
        b1.move(-vec)
        b2.move(vec)
    def create_balls(self):
        if pg.mouse.get_pressed()[0]==1:
            for i in range(ballsToCreatOnClick):
                ball=Ball(pg.mouse.get_pos())
                self.addBallToLis(ball)
            
    def indexOf(self,obj):
        x,y=obj.pos
        x=int(x//self.sides[0])
        y=int(y//self.sides[1])
        return x,y
    def addBallToLis(self,obj):
        index=self.indexOf(obj)
        obj.index=index
        self.lis[index[0]-1][index[1]-1].append(obj)
    def draw(self):
        for i in range(self.cells[0]):pg.draw.line(window,self.col,(i*self.sides[0],0),(i*self.sides[0],height))
        for i in range(self.cells[1]):pg.draw.line(window,self.col,(0,i*self.sides[1]),(width,i*self.sides[1]))
    def draw_balls(self):
        for x in range(self.cells[0]):
            for y in range(self.cells[1]):
                for ball in self.lis[x][y]:
                    ball.move()
                    index = self.indexOf(ball)
                    if not index==ball.index:
                        self.lis[x][y].remove(ball)
                        self.addBallToLis(ball)
                    ball.draw()
grid=Grid(30,30)
while run():
    # grid.draw()
    grid.draw_balls()
    grid.create_balls()
    grid.loop_screen()
    # grid.thread_loop_screen()
    

