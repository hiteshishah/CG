'''
Created on June 12, 2016

@author: Srinivas
'''

from SimpleCanvas import SimpleCanvas
from Rasterization import Rasterization

class LineTest(object):

    screenWidth = 600
    screenHeight = 600
    sc = SimpleCanvas()
    rast = Rasterization(600)

    #
    #   draw all the lines
    #
    # Idea for lettering style from:
    # http://patorjk.com/software/taag/#p=display&f=Star%20Wars&t=Type%20Something
    #          _______   ______
    #         /  ____|  /  __  \
    #        |  |  __  |  |  |  |
    #        |  | |_ | |  |  |  |
    #        |  |__| | |  `--'  |
    #         \______|  \______/
    #
    def lineTest(self):

        self.sc.setSize(self.screenWidth, self.screenHeight)
        self.sc.clear(self.sc.width,self.sc.height)

        self.sc.setColor(0, 255, 0) #Set Red Green and Blue color

        ######## The letter 'G' in green ########
        self.rast.drawLine(80, 260, 220,260, self.sc)  # Horizontal left to right
        self.rast.drawLine(40, 220,80,260, self.sc)   # 315 degree slope
        self.rast.drawLine(220, 260,260,220, self.sc) # 45 degree slope
        self.rast.drawLine(260, 220,260,160,self.sc) # Vertical bottom to top
        self.rast.drawLine(260,160,180,160,self.sc)  # Horizontal right to left
        self.rast.drawLine(180,160,180,200,self.sc)
        self.rast.drawLine(180,200,220,200,self.sc)
        self.rast.drawLine(220,200,200,220,self.sc)
        self.rast.drawLine(200, 220,100,220,self.sc)
        self.rast.drawLine(100,220,80,200,self.sc)
        self.rast.drawLine(80, 200,80,100,self.sc)
        self.rast.drawLine(80,100,100,80,self.sc)
        self.rast.drawLine(100,80,200,80,self.sc)
        self.rast.drawLine(200, 80,220,100,self.sc)
        self.rast.drawLine(220, 100,220,120,self.sc)
        self.rast.drawLine(220, 120,260,120,self.sc)
        self.rast.drawLine(260, 120,260,80,self.sc)
        self.rast.drawLine(260, 80,220,40,self.sc) # 135 degree slope
        self.rast.drawLine(220, 40,80,40,self.sc)
        self.rast.drawLine(80, 40,40,80,self.sc)    # 225 degree slope
        self.rast.drawLine(40, 80,40,220,self.sc)   # Vertical top to bottom

        ######## The letter 'O' in red ########

        self.sc.setColor(255, 0, 0) #Set Red Green and Blue color

        self.rast.drawLine(450, 280,520,260,self.sc) # 16.6 degree slope
        self.rast.drawLine(520, 260,540,240,self.sc) # 45 degree slope
        self.rast.drawLine(540, 240,560,150,self.sc) # 77.47 degree slope
        self.rast.drawLine(560, 150,540,60,self.sc) # 102.83 degree slope
        self.rast.drawLine(540, 60,520,40,self.sc) # 135 degree slope
        self.rast.drawLine(520, 40,450,20,self.sc) # 163.3 degree slope
        self.rast.drawLine(450, 20,380,40,self.sc) # 196.71 degree slope
        self.rast.drawLine(380, 40,360,60,self.sc) # 225 degree slope
        self.rast.drawLine(360,60,340,150,self.sc)
        self.rast.drawLine(340,150,360,240,self.sc)
        self.rast.drawLine(360,240,380,260,self.sc)
        self.rast.drawLine(380,260,450,280,self.sc)
        self.rast.drawLine(420,220,480,220,self.sc)
        self.rast.drawLine(480,220,520,180,self.sc)
        self.rast.drawLine(520,180,520,120,self.sc)
        self.rast.drawLine(520,120,480,80,self.sc)
        self.rast.drawLine(480, 80,420,80,self.sc)
        self.rast.drawLine(420,80,380,120,self.sc)
        self.rast.drawLine(380,120,380,180,self.sc)
        self.rast.drawLine(380, 180,420,220, self.sc)

        #draw the students initials
        self.rast.myInitials (self.sc)

        self.sc.showImage()

if __name__ == "__main__":
    ltObj = LineTest()
    ltObj.lineTest()
