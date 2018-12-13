'''
@author: Hiteshi Shah
'''

from SimpleCanvas import SimpleCanvas
from Rasterization import Rasterization

class FillTest(object):

    screenWidth = 901
    screenHeight = 601
    sc = SimpleCanvas()
    rast = Rasterization(601)

    def filltest(self):
        x = [0,0,0,0,0,0,0,0,0,0]
        y = [0,0,0,0,0,0,0,0,0,0]
        self.sc.setSize(self.screenWidth, self.screenHeight)
        self.sc.clear(self.sc.width,self.sc.height)

        self.sc.setColor(255, 0, 0) #Set Red Green and Blue color

        ########### TEAPOT START ###########
        # BASE
        x[0] = 760
        y[0] = 40
        x[1] = 600
        y[1] = 40
        x[2] = 620
        y[2] = 60
        x[3] = 740
        y[3] = 60
        self.rast.drawPolygon(4,x,y,self.sc)

        #RIGHT BOTTOM TRIANGLE

        x[0] = 800
        y[0] = 120
        x[1] = 740
        y[1] = 60
        x[2] = 620
        y[2] = 60
        self.sc.setColor(230,0,0)
        self.rast.drawPolygon(3,x,y,self.sc)

        #SPOUT

        x[0] = 620
        y[0] = 60
        x[1] = 560
        y[1] = 100
        x[2] = 500
        y[2] = 180
        self.sc.setColor(204,0,0)
        self.rast.drawPolygon(3,x,y,self.sc)

        x[0] = 620
        y[0] = 60
        x[1] = 500
        y[1] = 180
        x[2] = 460
        y[2] = 200
        x[3] = 520
        y[3] = 200
        x[4] = 580
        y[4] = 160
        self.sc.setColor(179,0,0)
        self.rast.drawPolygon(5,x,y,self.sc)

        x[0] = 620
        y[0] = 60
        x[1] = 580
        y[1] = 160
        x[2] = 620
        y[2] = 240
        x[3] = 740
        y[3] = 240
        x[4] = 800
        y[4] = 120
        self.sc.setColor(153,0,0)
        self.rast.drawPolygon(5,x,y,self.sc)

        x[0] = 800
        y[0] = 120
        x[1] = 840
        y[1] = 160
        x[2] = 855
        y[2] = 200
        x[3] = 720
        y[3] = 220
        x[4] = 720
        y[4] = 200
        x[5] = 830
        y[5] = 190
        x[6] = 825
        y[6] = 165
        x[7] = 780
        y[7] = 120
        self.sc.setColor(128,0,0)
        self.rast.drawPolygon(8,x,y,self.sc)

        x[0] = 690
        y[0] = 240
        x[1] = 710
        y[1] = 260
        x[2] = 650
        y[2] = 260
        x[3] = 670
        y[3] = 240
        self.sc.setColor(102,0,0)
        self.rast.drawPolygon(4,x,y,self.sc)

        ######## TRIANGLE #######
        x[0] = 460
        y[0] = 220
        x[1] = 490
        y[1] = 280
        x[2] = 420
        y[2] = 280
        self.sc.setColor(0,255,0)
        self.rast.drawPolygon(3,x,y,self.sc)

        ########## QUAD ##########
        x[0] = 380
        y[0] = 280
        x[1] = 320
        y[1] = 320
        x[2] = 360
        y[2] = 380
        x[3] = 420
        y[3] = 340
        self.sc.setColor(0,204,204)
        self.rast.drawPolygon(4,x,y,self.sc)

        ############ STAR #############
        #RIGHT SIDE
        x[0] = 230
        y[0] = 389
        x[1] = 260
        y[1] = 369
        x[2] = 254
        y[2] = 402
        x[3] = 278
        y[3] = 425
        x[4] = 245
        y[4] = 430
        x[5] = 230
        y[5] = 460
        x[6] = 230
        y[6] = 410
        self.sc.setColor(204,204,0)
        self.rast.drawPolygon(7,x,y,self.sc)

        #LEFT SIDE
        x[0] = 230
        y[0] = 460
        x[1] = 216
        y[1] = 430
        x[2] = 183
        y[2] = 425
        x[3] = 207
        y[3] = 402
        x[4] = 201
        y[4] = 369
        x[5] = 230
        y[5] = 389
        x[6] = 230
        y[6] = 410
        self.sc.setColor(179,179,0)
        self.rast.drawPolygon(7,x,y,self.sc)

        ########## BORDERS ###############
        #SQUARE BOTTOM LEFT

        x[0] = 0
        y[0] = 0
        x[1] = 0
        y[1] = 20
        x[2] = 20
        y[2] = 20
        x[3] = 20
        y[3] = 0
        self.sc.setColor(0,0,255)
        self.rast.drawPolygon(4,x,y,self.sc)

        x[0] = 0
        y[0] = 10
        x[1] = 10
        y[1] = 10
        x[2] = 10
        y[2] = 580
        x[3] = 0
        y[3] = 580
        self.sc.setColor(0,26,230)
        self.rast.drawPolygon(4,x,y,self.sc)

        x[0] = 0
        y[0] = 580
        x[1] = 0
        y[1] = 600
        x[2] = 20
        y[2] = 600
        x[3] = 20
        y[3] = 580
        self.sc.setColor(0,51,204)
        self.rast.drawPolygon(4,x,y,self.sc)

        #TRIANGLE TOP:TOP
        x[0] = 10
        y[0] = 590
        x[1] = 10
        y[1] = 600
        x[2] = 880
        y[2] = 600
        self.sc.setColor(0,77,179)
        self.rast.drawPolygon(3,x,y,self.sc)

        #TRIANGLE TOP:BOTTOM
        x[0] = 10
        y[0] = 590
        x[1] = 880
        y[1] = 590
        x[2] = 880
        y[2] = 600
        self.sc.setColor(0,102,153)
        self.rast.drawPolygon(3,x,y,self.sc)

        #SQUARE TOP RIGHT
        x[0] = 900
        y[0] = 600
        x[1] = 900
        y[1] = 580
        x[2] = 880
        y[2] = 580
        x[3] = 880
        y[3] = 600
        self.sc.setColor(26,102,128)
        self.rast.drawPolygon(4,x,y,self.sc)

        #TRIANGLE RIGHT:RIGHT
        x[0] = 890
        y[0] = 580
        x[1] = 900
        y[1] = 580
        x[2] = 890
        y[2] = 20
        self.sc.setColor(51,102,102)
        self.rast.drawPolygon(3,x,y,self.sc)

        #TRIANGLE RIGHT:LEFT
        x[0] = 900
        y[0] = 580
        x[1] = 900
        y[1] = 20
        x[2] = 890
        y[2] = 20
        self.sc.setColor(77,102,77)
        self.rast.drawPolygon(3,x,y,self.sc)

        #SQUARE BOTTOM RIGHT
        x[0] = 900
        y[0] = 0
        x[1] = 900
        y[1] = 20
        x[2] = 880
        y[2] = 20
        x[3] = 880
        y[3] = 0
        self.sc.setColor(102,102,51)
        self.rast.drawPolygon(4,x,y,self.sc)

        #QUAD BOTTOM
        x[0] = 20
        y[0] = 0
        x[1] = 20
        y[1] = 10
        x[2] = 880
        y[2] = 10
        x[3] = 880
        y[3] = 0
        self.sc.setColor(102,128,26)
        self.rast.drawPolygon(4,x,y,self.sc)

        self.sc.showImage()


if __name__ == "__main__":
    ftObj = FillTest()
    ftObj.filltest()