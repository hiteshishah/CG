from simpleCanvas import simpleCanvas
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
from numpy import zeros, uint8


class extendedCanvas(simpleCanvas):

    poly_fill = []
    poly_draw = []
    poly_fill_color = []
    poly_draw_color = []

    def __init__(self,w,h):
        self.setSize(w,h)


    def printLoop(self, n, x, y):
        verts = list(zip(x,y))
        p = Polygon(verts,closed=True, fill=False, edgecolor=[self.red, self.green, self.blue])
        self.poly_draw.append(p)
        self.poly_draw_color.append([self.red, self.green, self.blue])

    def printPoly(self,n, x, y):
        verts = list(zip(x,y))
        p = Polygon(verts,closed=True, fill=True,facecolor=[self.red, self.green, self.blue], edgecolor=[self.red, self.green, self.blue])
        self.poly_fill.append(p)
        self.poly_fill_color.append([self.red, self.green, self.blue])

    def showImage(self):

        plt.figure()

        axes = plt.gca()

        plt.imshow(self.img)
        for i1 in range(0,len(self.poly_draw)):
            axes.add_patch(self.poly_draw[i1])

        for i2 in range(0,len(self.poly_fill)):
            axes.add_patch(self.poly_fill[i2])
        plt.gca().invert_yaxis()
        plt.show()



# hept1x = [120,140,160,160,140,120,110]
# hept1y = [70,70,80,100,110,100,90]
# b = zip(hept1x,hept1y)
# p = Polygon(b)
#
# plt.figure()
# axes = plt.gca()
# img = zeros((300,300,3), dtype = uint8)
# imgObj = plt.imshow(img)
# plt.gca().invert_yaxis()
# axes.add_patch(Polygon(b,closed=True, fill=False, edgecolor=[0.7,0.7,0.7]))
# #plt.xlim([-10,10])
# #plt.ylim([-10,10])
# plt.show()
