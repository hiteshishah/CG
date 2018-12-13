'''
description: Midpoint Line Drawing algorithm
@author: Hiteshi Shah
'''

from SimpleCanvas import SimpleCanvas
import numpy as np

class Rasterization(object):

    scan_line = 0

    def __init__(self,n):
        self.scan_line = n


    def drawLine(self, x0, y0, x1, y1, sc):
        '''
        function to draw the line given by the specified co-ordinates using Midpoint Line Drawing algorithm
        :param x0: starting x-co-ordinate
        :param y0: starting y-co-ordinate
        :param x1: ending x-c-ordinate
        :param y1: ending y-co-ordinate
        :param sc: SimpleCanvas object
        '''

        # vertical line
        if x0 == x1:
            if y0 > y1:
                # to go from bottom to up
                y0, y1 = y1, y0
            x, y = x0, y0
            while y < y1:
                sc.setPixel(x, y)
                y += 1
        # horizontal line
        elif y0 == y1:
            if x0 > x1:
                # to go from left to right
                x0, x1 = x1, x0
            x, y = x0, y0
            while x < x1:
                sc.setPixel(x, y)
                x += 1
        # diagonal line
        elif abs(x1 - x0) == abs(y1 - y0):
            x, y = x0, y0
            while x != x1 and y != y1:
                sc.setPixel(x, y)
                x += np.sign(x1 - x0)
                y += np.sign(y1 - y0)
        else:
            dx = x1 - x0
            dy = y1 - y0

            # slope between 0 and 1
            if ((dx > 0 and dy > 0) or (dx < 0 and dy < 0)) and abs(dy) < abs(dx):
                dx = abs(dx)
                dy = abs(dy)
                d = 2 * dy - dx
                if x0 > x1:
                    x0, x1 = x1, x0
                    y0, y1 = y1, y0
                x, y = x0, y0
                while x < x1:
                    sc.setPixel(x, y)
                    x += 1
                    if d <= 0:
                        d += 2  * dy        # move east
                    else:
                        d += 2 * (dy - dx)  # move north-east
                        y += 1
            # slope greater than 1
            elif ((dx > 0 and dy > 0) or (dx < 0 and dy < 0)) and abs(dy) > abs(dx):
                dx = abs(dx)
                dy = abs(dy)
                d = 2 * dx - dy
                if y0 > y1:
                    x0, x1 = x1, x0
                    y0, y1 = y1, y0
                x, y = x0, y0
                while y < y1:
                    sc.setPixel(x, y)
                    y += 1
                    if d <= 0:
                        d += 2 * dx             # move north
                    else:
                        d += 2 * (dx - dy)      # move north-east
                        x += 1
            # slope between -1 and 0
            elif ((dx > 0 and dy < 0) or (dx < 0 and dy > 0)) and abs(dx) > abs(dy):
                dx = abs(dx)
                dy = abs(dy)
                d = 2 * dy - dx
                if x0 > x1:
                    x0, x1 = x1, x0
                    y0, y1 = y1, y0
                x, y = x0, y0
                while x < x1:
                    sc.setPixel(x, y)
                    x += 1
                    if d <= 0:
                        d += 2 * dy         # move west
                    else:
                        d += 2 * (dy - dx)  # move north-west
                        y -= 1
            # slope less than -1
            else:
                dx = abs(dx)
                dy = abs(dy)
                d = 2 * dx - dy
                if y0 > y1:
                    x0, x1 = x1, x0
                    y0, y1 = y1, y0
                x, y = x0, y0
                while y < y1:
                    sc.setPixel(x, y)
                    y += 1
                    if d <= 0:
                        d += 2 * dx         # move north
                    else:
                        d += 2 * (dx - dy)   # move north-west
                        x -= 1

    def myInitials (self, sc):

        # setting the color to blue
        sc.setColor (0, 0, 255)

        # drawing the letter 'H' in blue
        self.drawLine(40, 320, 40, 540, sc)
        self.drawLine(40, 320, 90, 320, sc)
        self.drawLine(90, 320, 90, 410, sc)
        self.drawLine(40, 540, 90, 540, sc)
        self.drawLine(90, 540, 90, 450, sc)
        self.drawLine(90, 450, 200, 450, sc)
        self.drawLine(90, 410, 200, 410, sc)
        self.drawLine(200, 410, 200, 320, sc)
        self.drawLine(200, 450, 200, 540, sc)
        self.drawLine(200, 320, 250, 320, sc)
        self.drawLine(200, 540, 250, 540, sc)
        self.drawLine(250, 320, 250, 540, sc)

        # drawing the letter 'S' in blue
        self.drawLine(540, 320, 540, 370, sc)
        self.drawLine(540, 320, 400, 320, sc)
        self.drawLine(400, 320, 350, 345, sc)
        self.drawLine(350, 345, 350, 430, sc)
        self.drawLine(350, 430, 400, 455, sc)
        self.drawLine(540, 370, 400, 370, sc)
        self.drawLine(400, 370, 400, 410, sc)
        self.drawLine(400, 410, 490, 410, sc)
        self.drawLine(490, 410, 540, 435, sc)
        self.drawLine(400, 455, 485, 455, sc)
        self.drawLine(540, 435, 540, 520, sc)
        self.drawLine(540, 520, 490, 555, sc)
        self.drawLine(490, 555, 350, 555, sc)
        self.drawLine(350, 555, 350, 505, sc)
        self.drawLine(350, 505, 485, 505, sc)
        self.drawLine(485, 505, 485, 455, sc)