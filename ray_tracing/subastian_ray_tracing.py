import pygame as pg
import numpy as np
from math import cos,sin,tan,cosh

dist = lambda p,q:sum((p-q)**2)**0.5
mag = lambda v:dist(v,np.zeros(v.size))
normalize = lambda v:v/mag(v)

class MainCamera:
    def __init__(self, pyg, x,y):
        self.pos=np.zeros(3)
        self.dir=normalize(np.ones(3))
        self.resolution=np.array([x, y])
        self.side_x = int(pyg.width/self.resolution[0])
        self.side_y = int(pyg.height/self.resolution[1])
        self.field_of_view = 50
        self.nearClipPlane=10
        self.aspect_ratio=1
        self.a=0
        self.b=0
        self.x=normalize(np.array([cos(self.a),sin(self.a),0]))
        self.y=normalize(np.array([0,cos(self.b),sin(self.b)]))
        self.z=normalize(np.cross(self.x,self.y))
    def render(self,pyg, objects):
        planeHeight=self.nearClipPlane*tan(self.field_of_view*0.5*(3.141596/180))*2
        planeWidth =planeHeight*self.aspect_ratio

        bottomLeftLocal = np.array([-planeWidth/2,-planeHeight/2,self.nearClipPlane])
        for i in range(self.resolution[0]):
            for j in range(self.resolution[1]):
                tx= i/(self.resolution[0]-1)
                ty= j/(self.resolution[1]-1)

                pointLocal = bottomLeftLocal + np.array([planeWidth*tx,planeHeight*ty,0])
                point = self.pos+self.x*pointLocal[0]+self.y*pointLocal[1]+self.z*pointLocal[2]
                dir = normalize(point-self.pos)
                col=self.ray_trace(dir,objects)
                col = np.array([np.dot(dir,np.array([1,0,0])),np.dot(dir,np.array([0,1,0])),np.dot(dir,np.array([0,0,1]))])
                pg.draw.rect(pyg.window, pyg.clipArray(col*255,0,255),[i*self.side_x,j*self.side_y,self.side_x,self.side_y],0)
    def ray_trace(self,dir,objects):
        for object in objects:
            value = object.intersect(self.pos,dir)
            return value
    def move(self,pyg):
        if "left" in pyg.buttons:self.a+=0.1
        elif "right" in pyg.buttons:self.a-=0.1
        elif "up" in pyg.buttons:self.b+=0.1
        elif "down" in pyg.buttons:self.b-=0.1
        self.change_dir()
    def change_dir(self):
        self.x=normalize(np.array([cos(self.a),sin(self.a),0]))
        self.y=normalize(np.array([0,cos(self.b),sin(self.b)]))
        self.z=normalize(np.cross(self.x,self.y))
                
class Object:
    def __init__(self,pos,col,is_light):
        self.pos=np.array(pos)
        self.col=np.array(col)
        self.in_light=is_light

class Sphere(Object):
    def __init__(self,pos,radi,col,is_light=False):
        Object.__init__(self,pos,col,is_light)
        self.radi=radi
    def intersect(self,pos,dir):
        r=self.pos-pos
        rn=normalize(r)
        dot=dir[0]*rn[0]+dir[1]*rn[1]
        rm=mag(r)
        t=cosh(dot/rm)
        c=((rm**2)-(t**2))**0.5
        if c<=self.radi:return np.ones(3)

        return np.zeros(3)

class Pyg:
    def __init__(self, x=0,y=0):
        if x==0 and y==0:self.window=pg.display.set_mode((0,0),  pg.FULLSCREEN)
        else:self.window=pg.display.set_mode((x,y))
        self.width,self.height=self.window.get_size()
        self.buttons=[]
    def clipArray(self,v, mini,maxi):
        nv=[]
        for i in v:
            if i<mini:nv.append(mini)
            elif i>maxi:nv.append(maxi)
            else:nv.append(i)
        return np.array(nv)
    def update(self):
        self.buttons.clear()
        pg.display.update()
        self.window.fill("Black")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    return False
                if event.key==pg.K_LEFT:self.buttons.append("left")
                if event.key==pg.K_RIGHT:self.buttons.append("right")
                if event.key==pg.K_UP:self.buttons.append("up")
                if event.key==pg.K_DOWN:self.buttons.append("down")
        return True

pyg=Pyg(600,600)
camera = MainCamera(pyg,30,30)

objectsInScene = [Sphere([0,0,6],5,[1,0,0])]

while pyg.update():
    camera.render(pyg,objectsInScene)
    camera.move(pyg)