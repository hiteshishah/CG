'''
Created on July 10, 2016

@author: Srinivas
'''


from cgCanvas import cgCanvas
import sys


class midtermMain(object):

    cgCanObj = None
    displayNumber = 1

    triangle = 0
    square = 0
    octagon = 0
    star = 0
    R = 0
    I = 0
    T = 0
    H = 0

    drawHeight = 500
    drawWidth = 500

    def __init__(self, w, h):


        self.cgCanObj = cgCanvas(w,h)
        cid1 = self.cgCanObj.fig.canvas.mpl_connect('key_press_event',self.on_key)
        cid2 = self.cgCanObj.fig.canvas.mpl_connect('button_press_event',self.on_click)
        self.drawHeight = h
        self.drawWidth = w


        # load all of your polygons
        x = [None] * 12
        y = [None] * 12

        #Triangle
        x[0] = 25
        y[0] = 125
        x[1] = 75
        y[1] = 125
        x[2] = 50
        y[2] = 175
        self.triangle = self.cgCanObj.addPoly(x, y, 3)

        #square
        x[0] = 125.0
        y[0] = 125.0
        x[1] = 175.0
        y[1] = 125.0
        x[2] = 175.0
        y[2] = 175.0
        x[3] = 125.0
        y[3] = 175.0
        self.square = self.cgCanObj.addPoly(x, y, 4)

        #Octagon
        x[0] = 25.0
        y[0] = 25.0
        x[1] = 35.0
        y[1] = 15.0
        x[2] = 55.0
        y[2] = 15.0
        x[3] = 75.0
        y[3] = 25.0
        x[4] = 75.0
        y[4] = 55.0
        x[5] = 55.0
        y[5] = 75.0
        x[6] = 35.0
        y[6] = 75.0
        x[7] = 25.0
        y[7] = 55.0
        self.octagon = self.cgCanObj.addPoly(x, y, 8)

        #star
        x[0] = 150.0
        y[0] = 90.0
        x[1] = 140.0
        y[1] = 65.0
        x[2] = 110.0
        y[2] = 65.0
        x[3] = 140.0
        y[3] = 40.0
        x[4] = 110.0
        y[4] = 10.0
        x[5] = 150.0
        y[5] = 25.0
        x[6] = 190.0
        y[6] = 10.0
        x[7] = 160.0
        y[7] = 40.0
        x[8] = 190.0
        y[8] = 65.0
        x[9] = 160.0
        y[9] = 65.0
        self.star = self.cgCanObj.addPoly(x, y, 10)

        #R
        x[0] = 10.0
        y[0] = 480.0
        x[1] = 140.0
        y[1] = 480.0
        x[2] = 175.0
        y[2] = 450.0
        x[3] = 175.0
        y[3] = 430.0
        x[4] = 140.0
        y[4] = 370.0
        x[5] = 90.0
        y[5] = 370.0
        x[6] = 175.0
        y[6] = 140.0
        x[7] = 145.0
        y[7] = 140.0
        x[8] = 65.0
        y[8] = 370.0
        x[9] = 35.0
        y[9] = 370.0
        x[10] = 35.0
        y[10] = 140.0
        x[11] = 10.0
        y[11] = 140.0
        self.R = self.cgCanObj.addPoly(x, y, 12)

        #I
        x[0] = 190.0
        y[0] = 480.0
        x[1] = 340.0
        y[1] = 480.0
        x[2] = 340.0
        y[2] = 440.0
        x[3] = 280.0
        y[3] = 440.0
        x[4] = 280.0
        y[4] = 180.0
        x[5] = 340.0
        y[5] = 180.0
        x[6] = 340.0
        y[6] = 140.0
        x[7] = 190.0
        y[7] = 140.0
        x[8] = 190.0
        y[8] = 180.0
        x[9] = 250.0
        y[9] = 180.0
        x[10] = 250.0
        y[10] = 440.0
        x[11] = 190.0
        y[11] = 440.0
        self.I = self.cgCanObj.addPoly(x, y, 12)

        x = [None] * 12
        y = [None] * 12

        #T
        x[0] = 360.0
        y[0] = 480.0
        x[1] = 480.0
        y[1] = 480.0
        x[2] = 480.0
        y[2] = 440.0
        x[3] = 430.0
        y[3] = 440.0
        x[4] = 430.0
        y[4] = 140.0
        x[5] = 400.0
        y[5] = 140.0
        x[6] = 400.0
        y[6] = 440.0
        x[7] = 360.0
        y[7] = 440.0
        self.T = self.cgCanObj.addPoly(x, y, 8)

        x = [None] * 12
        y = [None] * 12

        #H (hole in R)
        x[0] = 35.0
        y[0] = 450.0
        x[1] = 110.0
        y[1] = 450.0
        x[2] = 130.0
        y[2] = 430.0
        x[3] = 110.0
        y[3] = 410.0
        x[4] = 35.0
        y[4] = 410.0
        self.H = self.cgCanObj.addPoly(x, y, 5)

    def on_key(self, event):

        key = event.key
        if key == 'Q' or key == 'q':
            sys.exit(0)

        elif key == 'P' or key =='p' or key == '1':
            self.displayNumber = 1

        elif key == 'C' or key =='c' or key == '2':
            self.displayNumber = 2

        elif key == 'T' or key == 't' or key == '3':
            self.displayNumber = 3

        elif key == 'V' or key == 'v' or key =='4':
            self.displayNumber = 0

        self.redraw()


    def on_click(self, event):
        self.displayNumber += 1
        self.redraw()

    #Function that draws the entire content of the modeled world
    def drawPolysNorm(self):

        # Draw a dark blue/purple triangle

        self.cgCanObj.clearTransform()
        self.cgCanObj.setColor(0.25, 0.0, 0.74)
        self.cgCanObj.drawPoly(self.triangle)

        # Draw a green square
        self.cgCanObj.setColor(0.0, 0.9, 0.08)
        self.cgCanObj.drawPoly(self.square)

        #Draw a pink otcagon
        self.cgCanObj.setColor(0.98, 0.0, 0.48)
        self.cgCanObj.drawPoly(self.octagon)

        #Draw a green star
        self.cgCanObj.setColor(0.68, 0.0, 0.75)
        self.cgCanObj.drawPoly(self.star)

    def drawPolysXform(self):

        #Draw a dark blue/purple triangle rotated
        self.cgCanObj.clearTransform()
        self.cgCanObj.rotate(-25.0)
        self.cgCanObj.setColor(0.25,0.0,0.74)

        self.cgCanObj.drawPoly(self.triangle)

        #Draw a green square translated
        self.cgCanObj.clearTransform()
        self.cgCanObj.translate(80.0, 75.0)
        self.cgCanObj.setColor(0.0,0.91,0.08)

        self.cgCanObj.drawPoly(self.square)

        #Draw a pink octagon scaled
        self.cgCanObj.clearTransform()
        self.cgCanObj.scale(0.75,0.5)
        self.cgCanObj.setColor(0.98,0.0,0.48)

        self.cgCanObj.drawPoly(self.octagon)

        #Draw a green star translated, scaled, rotated, then scaled back
        self.cgCanObj.clearTransform()
        self.cgCanObj.translate(50.0, 50.0)
        self.cgCanObj.scale(2.0,2.0)
        self.cgCanObj.rotate(-10.0)
        self.cgCanObj.translate(-50.0, 50.0)
        self.cgCanObj.setColor(0.68,0.0,0.75)

        self.cgCanObj.drawPoly(self.star)

    #Draw RIT Letters
    def drawLetters(self):

        #Draw the staggered translation
        self.cgCanObj.clearTransform()
        self.cgCanObj.translate(15.0, 0.0)
        self.cgCanObj.drawPoly(self.R)

        self.cgCanObj.clearTransform()
        self.cgCanObj.translate(10.0, 0.0)
        self.cgCanObj.drawPoly(self.I)

        self.cgCanObj.clearTransform()
        self.cgCanObj.translate(5.0, 0.0)
        self.cgCanObj.drawPoly(self.T)

        self.cgCanObj.clearTransform()
        self.cgCanObj.translate(15.0, 0.0)
        self.cgCanObj.setColor(0.0,0.0,0.0)
        self.cgCanObj.drawPoly(self.H)


    def redraw(self):

        #set clear color to black
        self.cgCanObj.setColor(0.0, 0.0, 0.0)
        self.cgCanObj.clear(self.drawWidth , self.drawHeight)

        #Plain old polygon test
        if self.displayNumber % 4 == 1:
            self.cgCanObj.setClipWindow(0.0, 500.0, 0.0, 500.0)
            self.cgCanObj.setViewport(0,0,self.drawWidth, self.drawHeight)
            self.drawPolysNorm()

        elif self.displayNumber % 4 == 2:
            self.cgCanObj.setClipWindow(35.0,175.0,35.0,165.0)
            self.cgCanObj.setViewport(0,0,self.drawWidth, self.drawHeight)

            self.drawPolysNorm()

        elif self.displayNumber % 4 == 3:
            self.cgCanObj.setClipWindow(0,500,0,500)
            self.cgCanObj.setViewport(0,0,self.drawWidth, self.drawHeight)

            #draw the transformed polys
            self.drawPolysXform()
        else:

            self.cgCanObj.setClipWindow(0.0,500.0,0.0,500.0)
            #self.cgCanObj.setColor(0.98,0.31,0.08)
            #self.drawLetters()

            wdiff = self.drawWidth / 3
            hdiff = self.drawHeight / 3

            # will use xaspect and yaspect to
            # draw each row with a different ratio
            xaspect = self.drawWidth / 3
            yaspect = self.drawHeight / 3
            x = 0
            y = 0

            for i in range(0,3):
                #adjust y aspect
                yaspect = hdiff/ (i+1)

                for j in range(0,3):
                    #lets play around with colors
                    if i == j:
                        self.cgCanObj.setColor(0.98,0.31,0.08)
                    elif i < j:
                        self.cgCanObj.setColor(0.0,0.91, 0.08)
                    else:  #i > j xaspect larger
                        self.cgCanObj.setColor(0.98,0.0,0.48)

                    xaspect = wdiff / (j+1)
                    self.cgCanObj.setViewport(x, y, xaspect, yaspect)
                    self.drawLetters()
                    x += wdiff + 35

                y += hdiff +35
                xaspect = wdiff
                x = 0

        self.cgCanObj.drawnow()

    #THe display function
    def doDraw(self):

        #set clear color to black
        self.cgCanObj.setColor(0.0, 0.0, 0.0)
        self.cgCanObj.clear(self.drawWidth , self.drawHeight)

        #Plain old polygon test
        if self.displayNumber % 4 == 1:
            self.cgCanObj.setClipWindow(0.0, 500.0, 0.0, 500.0)
            self.cgCanObj.setViewport(0,0,self.drawWidth, self.drawHeight)
            self.drawPolysNorm()

        elif self.displayNumber % 4 == 2:
            self.cgCanObj.setClipWindow(35.0,175.0,35.0,165.0)
            self.cgCanObj.setViewport(0,0,self.drawWidth, self.drawHeight)

            self.drawPolysNorm()

        elif self.displayNumber % 4 == 3:
            self.cgCanObj.setClipWindow(0,500,0,500)
            self.cgCanObj.setViewport(0,0,self.drawWidth, self.drawHeight)

            #draw the transformed polys
            self.drawPolysXform()
        else:

            self.cgCanObj.setClipWindow(0.0,500.0,0.0,500.0)
            #self.cgCanObj.setColor(0.98,0.31,0.08)
            #self.drawLetters()

            wdiff = self.drawWidth / 3
            hdiff = self.drawHeight / 3

            # will use xaspect and yaspect to
            # draw each row with a different ratio
            xaspect = self.drawWidth / 3
            yaspect = self.drawHeight / 3
            x = 0
            y = 0

            for i in range(0,3):
                #adjust y aspect
                yaspect = hdiff/ (i+1)

                for j in range(0,3):
                    #lets play around with colors
                    if i == j:
                        self.cgCanObj.setColor(0.98,0.31,0.08)
                    elif i < j:
                        self.cgCanObj.setColor(0.0,0.91, 0.08)
                    else:  #i > j xaspect larger
                        self.cgCanObj.setColor(0.98,0.0,0.48)

                    xaspect = wdiff / (j+1)
                    self.cgCanObj.setViewport(x, y, xaspect, yaspect)
                    self.drawLetters()
                    x += wdiff + 35

                y += hdiff +35
                xaspect = wdiff
                x = 0

        self.cgCanObj.showImage()


if __name__ == "__main__":
    ctObj = midtermMain(500,500)
    ctObj.doDraw()