'''
Created on June 12, 2016

@author: Srinivas
'''

from extendedCanvas import extendedCanvas
from clipper import clipper

class clipTest(object):

    screenWidth = 300
    screenHeight = 300
    ec = extendedCanvas(screenWidth,screenHeight)
    clip = clipper()

    def __init__(self):
        pass

    def drawClipRegion(self,llx,lly,urx,ury):

        x = [llx,urx,urx,llx]
        y = [lly,lly,ury,ury]

        self.ec.printLoop(4,x,y)


    def cliptest(self):

        self.ec.setColor(0,0,0)
        self.ec.clear(self.screenWidth, self.screenHeight)

        quad1x = [20,20,40,40]
        quad1y = [120,140,140,120]

        quad2x = [80,80,60,60]
        quad2y = [160,200,200,160]

        quad3x = [20,50,50,20]
        quad3y = [60,60,50,50]

        quad4x = [44,60,60,44]
        quad4y = [122,122,146,146]

        pent1x = [80,90,110,100,80]
        pent1y = [20,10,20,50,40]

        hept1x = [120,140,160,160,140,120,110]
        hept1y = [70,70,80,100,110,100,90]
        
        nona1x = [190,230,247,269,284,251,233,212,203]
        nona1y = [56,68,56,71,104,122,110,119,95]
        
        deca1x = [177, 222, 267, 250, 294, 240, 222, 204, 150, 194]
        deca1y = [156, 188,156,207, 240, 240, 294, 240, 240, 207]

        self.ec.setColor(1,1,1)
        self.drawClipRegion(10,110,50,150)
        self.drawClipRegion(30,10,70,80)
        self.drawClipRegion(90,34,120,60)
        self.drawClipRegion(90,80,130,110)
        self.drawClipRegion(221, 80, 251, 101)
        self.drawClipRegion(198, 198, 276, 258)

        wx = [None] * 50
        wy = [None] * 50
        #
        # first polygon:  entirely within region
        #
        wl = 0
        wl = self.clip.clipPolygon(4,quad1x,quad1y,wx,wy,10,110,50,150)
        self.ec.setColor(1,0,0)
        self.ec.printLoop(4, quad1x,quad1y)
        self.ec.printPoly(wl,wx,wy)

        #
        # second polygon:  entirely outside region
        #
        wl = 0
        self.ec.setColor(0,1,0)
        self.ec.printLoop(4, quad2x, quad2y)
        wl = self.clip.clipPolygon(4, quad2x, quad2y, wx, wy, 10, 110, 50, 150)
        #Should not draw anything
        if(wl > 0):
            self.ec.printPoly(wl,wx,wy)

        #
        # third polygon: halfway outside on left
        #
        wl = 0
        wl = self.clip.clipPolygon(4, quad3x, quad3y, wx, wy, 30, 10, 70, 80)
        self.ec.setColor(0,0,1)
        self.ec.printLoop(4, quad3x, quad3y)
        self.ec.printPoly(wl, wx, wy)

        #
        # fourth polygon: part outside on right
        #
        wl = 0
        wl = self.clip.clipPolygon(4, quad4x, quad4y, wx, wy, 10, 110, 50, 150)
        self.ec.setColor(1,0,1)
        self.ec.printLoop(4, quad4x, quad4y)
        self.ec.printPoly(wl, wx, wy)


        # fifth polygon: outside on left and bottom
        #
        wl = 0
        wl = self.clip.clipPolygon(5, pent1x, pent1y, wx, wy, 90, 34, 120, 60)
        self.ec.setColor(1,0.5,1)
        self.ec.printLoop(5, pent1x, pent1y)
        self.ec.printPoly(wl, wx, wy)


        # sixth polygon: outside on top right and bottom
        #
        wl = 0
        wl = self.clip.clipPolygon(7, hept1x, hept1y, wx, wy, 90, 80, 130, 110)
        self.ec.setColor(0.7,0.7,0.7)
        self.ec.printLoop(7, hept1x, hept1y)
        self.ec.printPoly(wl, wx, wy)

        #
        # seventh polygon: surrounds the clip region
        #
        wl = 0
        wx = [None] * 50
        wy = [None] * 50
        wl = self.clip.clipPolygon(9, nona1x, nona1y, wx, wy, 221, 80, 251, 101)
        self.ec.setColor(0.871,0.722,0.529)
        self.ec.printLoop(9, nona1x, nona1y)
        self.ec.printPoly(wl, wx, wy)

        #
        # eigth polygon: outside on all four edges
        #
        wl = 0
        wl = self.clip.clipPolygon(10, deca1x, deca1y, wx, wy, 198, 198, 276, 258)
        self.ec.setColor(1.0,0.64705, 0.0)
        self.ec.printLoop(10, deca1x, deca1y)
        self.ec.printPoly(wl, wx, wy)

        self.ec.showImage()

if __name__ == "__main__":
    ctObj = clipTest()
    ctObj.cliptest()



