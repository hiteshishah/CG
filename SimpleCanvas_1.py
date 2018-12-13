'''
Created on June 12, 2016

@author: Srinivas
'''

from pylab import imshow, show, plt , draw
from numpy import zeros, uint8

class SimpleCanvas(object):
    
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
        plt.axis('off')
        show()
    
    def setPixel(self,x, y):
        y,x = x,y
        self.img[x,y,0] = self.red
        self.img[x,y,1] = self.green
        self.img[x,y,2] = self.blue
    
    def clear(self,width,height):
        self.img = zeros((self.width,self.height,3), dtype = uint8)        
        
    def setColor(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b 
