import pygame as pg
import numpy as np
from math import cos,sin

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
        self.field_of_view = 1/2
        self.a=0
        self.b=0
        self.x=normalize(np.array([cos(self.a),sin(self.a),0]))
        self.y=normalize(np.array([0,cos(self.b),sin(self.b)]))
        self.z=normalize(np.cross(self.x,self.y))
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
    def render(self, pyg, objects):
        for y in range(self.resolution[1]):
            for x in range(self.resolution[0]):
                col = self.shoot_ray(x, y, objects)
                pg.draw.rect(pyg.window, pyg.clipArray(col*255,0,255),[x*self.side_x,y*self.side_y,self.side_x,self.side_y],0)
    def shoot_ray(self,x,y, objects):
        z=self.z*self.field_of_view
        x=(self.x*(1/self.resolution[0])*(x-(self.resolution[0]/2)))
        y=(self.y*(1/self.resolution[1])*(y-(self.resolution[1]/2)))
        p0=x+y+z
        vec=normalize(p0+self.pos)
        col=self.intersection(vec,objects)
        # return np.array([np.dot(vec,np.array([1,0,0])),np.dot(vec,np.array([0,1,0])),np.dot(vec,np.array([0,0,1]))])
        return col
    # def intersection(self,vec,objects):
    #     for object in objects:
    #         dit=(np.dot(self.pos,vec)**2)-(np.dot(self.pos,self.pos)-(object.radi*object.radi))
    #         print(dit)
    #         if dit<0:return np.zeros(3)
    #         return np.ones(3)
    #         # return (dit-np.dot(self.pos,vec))
    def intersection(self,vec,objects):
        for object in objects:
            mag(self.pos+(vec*t)-(object.pos-self.pos))=object.radi
                
class Object:
    def __init__(self,pos,col,is_light):
        self.pos=np.array(pos)
        self.col=np.array(col)
        self.in_light=is_light

class Sphere(Object):
    def __init__(self,pos,radi,col,is_light=False):
        Object.__init__(self,pos,col,is_light)
        self.radi=radi

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
camera = MainCamera(pyg,60,60)

objectsInScene = [Sphere([0,0,50],1,[1,0,0])]

while pyg.update():
    camera.render(pyg,objectsInScene)
    camera.move(pyg)