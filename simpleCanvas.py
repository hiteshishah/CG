'''
Created on June 12, 2016

@author: Srinivas
'''

from pylab import imshow, show, plt, draw, gca
from matplotlib.patches import Polygon
from numpy import zeros, uint8

class simpleCanvas(object):
    
    width = 600
    height = 600
    red = 0
    green = 0
    blue = 0
    img = zeros((width,height,3), dtype = uint8) 
    imgObj = []

    poly_draw = []
    poly_draw_color = []
    fig = None
    
    def __init__(self):
        pass

    
    def setSize(self, w, h):
        self.fig = plt.figure()
        self.width = w
        self.height = h
    
    def drawnow(self):

        plt.cla()

        imshow(self.img)
        axes = plt.gca()
        for i1 in range(0,len(self.poly_draw)):
            axes.add_patch(self.poly_draw[i1])

        plt.gca().invert_yaxis()
        plt.draw()
    
    def showImage(self):

        axes = self.fig.gca()
        self.imgObj = imshow(self.img)

        for i1 in range(0,len(self.poly_draw)):
            axes.add_patch(self.poly_draw[i1])

        self.fig.gca().invert_yaxis()
        show()

    def drawOutline(self, n, x, y):
        verts = zip(x,y)
        p = Polygon(verts,closed=True, fill=True, facecolor=[self.red, self.green, self.blue])
        self.poly_draw.append(p)
        self.poly_draw_color.append([self.red, self.green, self.blue])

    def setPixel(self,x, y):
        self.img[y,x,0] = int(self.red * 255)
        self.img[y,x,1] = int(self.green * 255)
        self.img[y,x,2] = int(self.blue * 255)
    
    def clear(self,width,height):
        self.img = zeros((self.height,self.width,3), dtype = uint8)
        self.poly_draw = []
        self.poly_draw_color = []
        
    def setColor(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b 
