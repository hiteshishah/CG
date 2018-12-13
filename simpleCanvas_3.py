'''
Created on June 12, 2016

@author: Srinivas
'''

from pylab import imshow, show, plt, draw, gca
from numpy import zeros, uint8

class simpleCanvas(object):
    
    width = 600
    height = 600
    red = 0
    green = 0
    blue = 0
    img = zeros((width,height,3), dtype = uint8) 
    imgObj = []
    
    def __init__(self):
        pass

    def setSize(self, w, h):
        self.width = w
        self.height = h
    
    def drawnow(self):
        self.imgObj.set_data(self.img)
        draw()
    
    def showImage(self):
        self.imgObj = imshow(self.img)
        plt.gca().invert_yaxis()
        show()
    
    def setPixel(self,x, y):
        self.img[y,x,0] = self.red
        self.img[y,x,1] = self.green
        self.img[y,x,2] = self.blue
    
    def clear(self,width,height):
        self.img = zeros((self.height,self.width,3), dtype = uint8)
        
    def setColor(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b 
