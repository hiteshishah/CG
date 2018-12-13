'''
//  tilt.py
//
//  Routines for tessellating the tilt of the lamp.
//
'''

from simpleShape import simpleShape
import math

class tilt(simpleShape):

    def __init__(self):
        pass

    def makeTilt(self, subdivisions):
        '''
        function to create a unit cube, centered at the origin, with a given number
        of subdivisions in each direction on each face
        :param subdivisions: the number of subdivisions in each direction on each face
        '''

        if (subdivisions < 1):
            subdivisions = 1

        # add your code here

        # initializing the co-ordinates for the face on the x-y plane when z = 0.5

        # the x, y, and z co-ordinates of the upper (top) triangle of the square
        up_x1 = -0.5
        up_y1 = 0.001
        up_z1 = 0.5
        up_x2 = -0.5
        up_y2 = -0.001
        up_z2 = 0.5
        up_x3 = 0.5
        up_y3 = 0.001
        up_z3 = 0.5

        # the x, y, and z co-ordinates of the lower (bottom) triangle of the square
        bot_x1 = 0.5
        bot_y1 = 0.001
        bot_z1 = 0.5
        bot_x2 = -0.5
        bot_y2 = -0.001
        bot_z2 = 0.5
        bot_x3 = 0.5
        bot_y3 = -0.001
        bot_z3 = 0.5

        # if the number of subdivisions is 1, draw the triangles
        if subdivisions == 1:
            try:
                nx1 = up_x1 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx1 = up_x1

            try:
                nx2 = up_x2 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx2 = up_x2

            try:
                nx3 = up_x3 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx3 = up_x3

            try:
                ny1 = up_y1 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny1 = up_y1

            try:
                ny2 = up_y2 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny2 = up_y2

            try:
                ny3 = up_y3 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny3 = up_y3

            try:
                nz1 = up_z1 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz1 = up_z1

            try:
                nz2 = up_z2 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz2 = up_z2

            try:
                nz3 = up_z3 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz3 = up_z3
            self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                             nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
            try:
                nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx1 = bot_x1

            try:
                nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx2 = bot_x2

            try:
                nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx3 = bot_x3

            try:
                ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny1 = bot_y1

            try:
                ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny2 = bot_y2

            try:
                ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny3 = bot_y3

            try:
                nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz1 = bot_z1

            try:
                nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz2 = bot_z2

            try:
                nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz3 = bot_z3
            self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                      nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
        # if the number of subdivisions is more than 1, iteratively divide the face into smaller triangles
        else:
            factor = abs(up_x1 - up_x3) / subdivisions

            up_y2 = up_y1 - factor
            up_x3 = up_x1 + factor

            bot_x1 = up_x3
            bot_y2 = up_y2
            bot_x3 = bot_x2 + factor
            bot_y3 = bot_y1 - factor

            try:
                nx1 = up_x1 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx1 = up_x1

            try:
                nx2 = up_x2 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx2 = up_x2

            try:
                nx3 = up_x3 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx3 = up_x3

            try:
                ny1 = up_y1 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny1 = up_y1

            try:
                ny2 = up_y2 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny2 = up_y2

            try:
                ny3 = up_y3 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny3 = up_y3

            try:
                nz1 = up_z1 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz1 = up_z1

            try:
                nz2 = up_z2 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz2 = up_z2

            try:
                nz3 = up_z3 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz3 = up_z3
            self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                             nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
            try:
                nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx1 = bot_x1

            try:
                nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx2 = bot_x2

            try:
                nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx3 = bot_x3

            try:
                ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny1 = bot_y1

            try:
                ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny2 = bot_y2

            try:
                ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny3 = bot_y3

            try:
                nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz1 = bot_z1

            try:
                nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz2 = bot_z2

            try:
                nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz3 = bot_z3
            self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                      nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)

            while not (round(bot_x3, 1) == 0.5 and round(bot_y3, 1) == -0.5):
                if round(bot_x3, 1) == 0.5:
                    up_y1 -= factor
                    up_y2 -= factor
                    up_y3 -= factor
                    bot_y1 -= factor
                    bot_y2 -= factor
                    bot_y3 -= factor

                    up_x1 = up_x1 + factor - 1
                    up_x2 = up_x2 + factor - 1
                    up_x3 = up_x3 + factor - 1
                    bot_x1 = bot_x1 + factor - 1
                    bot_x2 = bot_x2 + factor - 1
                    bot_x3 = bot_x3 + factor - 1
                else:
                    up_x1 += factor
                    up_x2 += factor
                    up_x3 += factor
                    bot_x1 += factor
                    bot_x2 += factor
                    bot_x3 += factor
                try:
                    nx1 = up_x1 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx1 = up_x1

                try:
                    nx2 = up_x2 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx2 = up_x2

                try:
                    nx3 = up_x3 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx3 = up_x3

                try:
                    ny1 = up_y1 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny1 = up_y1

                try:
                    ny2 = up_y2 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny2 = up_y2

                try:
                    ny3 = up_y3 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny3 = up_y3

                try:
                    nz1 = up_z1 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz1 = up_z1

                try:
                    nz2 = up_z2 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz2 = up_z2

                try:
                    nz3 = up_z3 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz3 = up_z3
                self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                                          nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
                try:
                    nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx1 = bot_x1

                try:
                    nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx2 = bot_x2

                try:
                    nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx3 = bot_x3

                try:
                    ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny1 = bot_y1

                try:
                    ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny2 = bot_y2

                try:
                    ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny3 = bot_y3

                try:
                    nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz1 = bot_z1

                try:
                    nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz2 = bot_z2

                try:
                    nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz3 = bot_z3
                self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                          nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)



        # initializing the co-ordinates for the face on the x-z plane when y = 0.5

        # the x, y, and z co-ordinates of the upper (top) triangle of the square
        up_x1 = -0.5
        up_y1 = 0.001
        up_z1 = -0.5
        up_x2 = -0.5
        up_y2 = 0.001
        up_z2 = 0.5
        up_x3 = 0.5
        up_y3 = 0.001
        up_z3 = -0.5

        # the x, y, and z co-ordinates of the lower (bottom) triangle of the square
        bot_x1 = 0.5
        bot_y1 = 0.001
        bot_z1 = -0.5
        bot_x2 = -0.5
        bot_y2 = 0.001
        bot_z2 = 0.5
        bot_x3 = 0.5
        bot_y3 = 0.001
        bot_z3 = 0.5

        # if the number of subdivisions is 1, draw the triangles
        if subdivisions == 1:
            try:
                nx1 = up_x1 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx1 = up_x1

            try:
                nx2 = up_x2 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx2 = up_x2

            try:
                nx3 = up_x3 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx3 = up_x3

            try:
                ny1 = up_y1 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny1 = up_y1

            try:
                ny2 = up_y2 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny2 = up_y2

            try:
                ny3 = up_y3 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny3 = up_y3

            try:
                nz1 = up_z1 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz1 = up_z1

            try:
                nz2 = up_z2 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz2 = up_z2

            try:
                nz3 = up_z3 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz3 = up_z3
            self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                             nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
            try:
                nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx1 = bot_x1

            try:
                nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx2 = bot_x2

            try:
                nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx3 = bot_x3

            try:
                ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny1 = bot_y1

            try:
                ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny2 = bot_y2

            try:
                ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny3 = bot_y3

            try:
                nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz1 = bot_z1

            try:
                nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz2 = bot_z2

            try:
                nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz3 = bot_z3
            self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                      nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
        # if the number of subdivisions is more than 1, iteratively divide the face into smaller triangles
        else:
            factor = abs(up_x1 - up_x3) / subdivisions

            up_z2 = up_z1 + factor
            up_x3 = up_x1 + factor

            bot_x1 = up_x3
            bot_z2 = up_z2
            bot_x3 = bot_x2 + factor
            bot_z3 = bot_z1 + factor

            try:
                nx1 = up_x1 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx1 = up_x1

            try:
                nx2 = up_x2 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx2 = up_x2

            try:
                nx3 = up_x3 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx3 = up_x3

            try:
                ny1 = up_y1 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny1 = up_y1

            try:
                ny2 = up_y2 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny2 = up_y2

            try:
                ny3 = up_y3 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny3 = up_y3

            try:
                nz1 = up_z1 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz1 = up_z1

            try:
                nz2 = up_z2 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz2 = up_z2

            try:
                nz3 = up_z3 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz3 = up_z3
            self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                             nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
            try:
                nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx1 = bot_x1

            try:
                nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx2 = bot_x2

            try:
                nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx3 = bot_x3

            try:
                ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny1 = bot_y1

            try:
                ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny2 = bot_y2

            try:
                ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny3 = bot_y3

            try:
                nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz1 = bot_z1

            try:
                nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz2 = bot_z2

            try:
                nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz3 = bot_z3
            self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                      nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)

            while not (round(bot_x3, 1) == 0.5 and round(bot_z3, 1) == 0.5):
                if round(bot_x3, 1) == 0.5:
                    up_z1 += factor
                    up_z2 += factor
                    up_z3 += factor
                    bot_z1 += factor
                    bot_z2 += factor
                    bot_z3 += factor

                    up_x1 = up_x1 + factor - 1
                    up_x2 = up_x2 + factor - 1
                    up_x3 = up_x3 + factor - 1
                    bot_x1 = bot_x1 + factor - 1
                    bot_x2 = bot_x2 + factor - 1
                    bot_x3 = bot_x3 + factor - 1
                else:
                    up_x1 += factor
                    up_x2 += factor
                    up_x3 += factor
                    bot_x1 += factor
                    bot_x2 += factor
                    bot_x3 += factor
                try:
                    nx1 = up_x1 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx1 = up_x1

                try:
                    nx2 = up_x2 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx2 = up_x2

                try:
                    nx3 = up_x3 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx3 = up_x3

                try:
                    ny1 = up_y1 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny1 = up_y1

                try:
                    ny2 = up_y2 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny2 = up_y2

                try:
                    ny3 = up_y3 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny3 = up_y3

                try:
                    nz1 = up_z1 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz1 = up_z1

                try:
                    nz2 = up_z2 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz2 = up_z2

                try:
                    nz3 = up_z3 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz3 = up_z3
                self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                                          nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
                try:
                    nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx1 = bot_x1

                try:
                    nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx2 = bot_x2

                try:
                    nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx3 = bot_x3

                try:
                    ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny1 = bot_y1

                try:
                    ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny2 = bot_y2

                try:
                    ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny3 = bot_y3

                try:
                    nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz1 = bot_z1

                try:
                    nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz2 = bot_z2

                try:
                    nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz3 = bot_z3
                self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                          nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)

        # initializing the co-ordinates for the face on the x-z plane when y = -0.5

        # the x, y, and z co-ordinates of the upper (top) triangle of the square
        up_x1 = -0.5
        up_y1 = -0.001
        up_z1 = 0.5
        up_x2 = -0.5
        up_y2 = -0.001
        up_z2 = -0.5
        up_x3 = 0.5
        up_y3 = -0.001
        up_z3 = 0.5

        # the x, y, and z co-ordinates of the lower (bottom) triangle of the square
        bot_x1 = 0.5
        bot_y1 = -0.001
        bot_z1 = 0.5
        bot_x2 = -0.5
        bot_y2 = -0.001
        bot_z2 = -0.5
        bot_x3 = 0.5
        bot_y3 = -0.001
        bot_z3 = -0.5

        # if the number of subdivisions is 1, draw the triangles
        if subdivisions == 1:
            try:
                nx1 = up_x1 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx1 = up_x1

            try:
                nx2 = up_x2 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx2 = up_x2

            try:
                nx3 = up_x3 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx3 = up_x3

            try:
                ny1 = up_y1 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny1 = up_y1

            try:
                ny2 = up_y2 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny2 = up_y2

            try:
                ny3 = up_y3 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny3 = up_y3

            try:
                nz1 = up_z1 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz1 = up_z1

            try:
                nz2 = up_z2 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz2 = up_z2

            try:
                nz3 = up_z3 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz3 = up_z3
            self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                             nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
            try:
                nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx1 = bot_x1

            try:
                nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx2 = bot_x2

            try:
                nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx3 = bot_x3

            try:
                ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny1 = bot_y1

            try:
                ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny2 = bot_y2

            try:
                ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny3 = bot_y3

            try:
                nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz1 = bot_z1

            try:
                nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz2 = bot_z2

            try:
                nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz3 = bot_z3
            self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                      nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
        # if the number of subdivisions is more than 1, iteratively divide the face into smaller triangles
        else:
            factor = abs(up_x1 - up_x3) / subdivisions

            up_z2 = up_z1 - factor
            up_x3 = up_x1 + factor

            bot_x1 = up_x3
            bot_z2 = up_z2
            bot_x3 = bot_x2 + factor
            bot_z3 = bot_z1 - factor

            try:
                nx1 = up_x1 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx1 = up_x1

            try:
                nx2 = up_x2 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx2 = up_x2

            try:
                nx3 = up_x3 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx3 = up_x3

            try:
                ny1 = up_y1 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny1 = up_y1

            try:
                ny2 = up_y2 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny2 = up_y2

            try:
                ny3 = up_y3 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny3 = up_y3

            try:
                nz1 = up_z1 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz1 = up_z1

            try:
                nz2 = up_z2 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz2 = up_z2

            try:
                nz3 = up_z3 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz3 = up_z3
            self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                             nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
            try:
                nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx1 = bot_x1

            try:
                nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx2 = bot_x2

            try:
                nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx3 = bot_x3

            try:
                ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny1 = bot_y1

            try:
                ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny2 = bot_y2

            try:
                ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny3 = bot_y3

            try:
                nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz1 = bot_z1

            try:
                nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz2 = bot_z2

            try:
                nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz3 = bot_z3
            self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                      nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)

            while not (round(bot_x3, 1) == 0.5 and round(bot_z3, 1) == -0.5):
                if round(bot_x3, 1) == 0.5:
                    up_z1 -= factor
                    up_z2 -= factor
                    up_z3 -= factor
                    bot_z1 -= factor
                    bot_z2 -= factor
                    bot_z3 -= factor

                    up_x1 = up_x1 + factor - 1
                    up_x2 = up_x2 + factor - 1
                    up_x3 = up_x3 + factor - 1
                    bot_x1 = bot_x1 + factor - 1
                    bot_x2 = bot_x2 + factor - 1
                    bot_x3 = bot_x3 + factor - 1
                else:
                    up_x1 += factor
                    up_x2 += factor
                    up_x3 += factor
                    bot_x1 += factor
                    bot_x2 += factor
                    bot_x3 += factor
                try:
                    nx1 = up_x1 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx1 = up_x1

                try:
                    nx2 = up_x2 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx2 = up_x2

                try:
                    nx3 = up_x3 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx3 = up_x3

                try:
                    ny1 = up_y1 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny1 = up_y1

                try:
                    ny2 = up_y2 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny2 = up_y2

                try:
                    ny3 = up_y3 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny3 = up_y3

                try:
                    nz1 = up_z1 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz1 = up_z1

                try:
                    nz2 = up_z2 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz2 = up_z2

                try:
                    nz3 = up_z3 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz3 = up_z3
                self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                                          nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
                try:
                    nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx1 = bot_x1

                try:
                    nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx2 = bot_x2

                try:
                    nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx3 = bot_x3

                try:
                    ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny1 = bot_y1

                try:
                    ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny2 = bot_y2

                try:
                    ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny3 = bot_y3

                try:
                    nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz1 = bot_z1

                try:
                    nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz2 = bot_z2

                try:
                    nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz3 = bot_z3
                self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                          nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)

        # initializing the co-ordinates for the face on the y-z plane when x = -0.5

        # the x, y, and z co-ordinates of the upper (top) triangle of the square
        up_x1 = -0.5
        up_y1 = 0.001
        up_z1 = -0.5
        up_x2 = -0.5
        up_y2 = -0.001
        up_z2 = -0.5
        up_x3 = -0.5
        up_y3 = 0.001
        up_z3 = 0.5

        # the x, y, and z co-ordinates of the lower (bottom) triangle of the square
        bot_x1 = -0.5
        bot_y1 = 0.001
        bot_z1 = 0.5
        bot_x2 = -0.5
        bot_y2 = -0.001
        bot_z2 = -0.5
        bot_x3 = -0.5
        bot_y3 = -0.001
        bot_z3 = 0.5

        # if the number of subdivisions is 1, draw the triangles
        if subdivisions == 1:
            try:
                nx1 = up_x1 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx1 = up_x1

            try:
                nx2 = up_x2 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx2 = up_x2

            try:
                nx3 = up_x3 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx3 = up_x3

            try:
                ny1 = up_y1 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny1 = up_y1

            try:
                ny2 = up_y2 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny2 = up_y2

            try:
                ny3 = up_y3 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny3 = up_y3

            try:
                nz1 = up_z1 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz1 = up_z1

            try:
                nz2 = up_z2 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz2 = up_z2

            try:
                nz3 = up_z3 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz3 = up_z3
            self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                             nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
            try:
                nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx1 = bot_x1

            try:
                nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx2 = bot_x2

            try:
                nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx3 = bot_x3

            try:
                ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny1 = bot_y1

            try:
                ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny2 = bot_y2

            try:
                ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny3 = bot_y3

            try:
                nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz1 = bot_z1

            try:
                nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz2 = bot_z2

            try:
                nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz3 = bot_z3
            self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                      nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
        # if the number of subdivisions is more than 1, iteratively divide the face into smaller triangles
        else:
            factor = abs(up_z1 - up_z3) / subdivisions

            up_y2 = up_y1 - factor
            up_z3 = up_z1 + factor

            bot_z1 = up_z3
            bot_y2 = up_y2
            bot_z3 = bot_z2 + factor
            bot_y3 = bot_y1 - factor

            try:
                nx1 = up_x1 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx1 = up_x1

            try:
                nx2 = up_x2 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx2 = up_x2

            try:
                nx3 = up_x3 / up_x1 + up_x2 + up_x3
            except ZeroDivisionError:
                nx3 = up_x3

            try:
                ny1 = up_y1 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny1 = up_y1

            try:
                ny2 = up_y2 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny2 = up_y2

            try:
                ny3 = up_y3 / up_y1 + up_y2 + up_y3
            except ZeroDivisionError:
                ny3 = up_y3

            try:
                nz1 = up_z1 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz1 = up_z1

            try:
                nz2 = up_z2 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz2 = up_z2

            try:
                nz3 = up_z3 / up_z1 + up_z2 + up_z3
            except ZeroDivisionError:
                nz3 = up_z3
            self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                             nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
            try:
                nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx1 = bot_x1

            try:
                nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx2 = bot_x2

            try:
                nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
            except ZeroDivisionError:
                nx3 = bot_x3

            try:
                ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny1 = bot_y1

            try:
                ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny2 = bot_y2

            try:
                ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
            except ZeroDivisionError:
                ny3 = bot_y3

            try:
                nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz1 = bot_z1

            try:
                nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz2 = bot_z2

            try:
                nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
            except ZeroDivisionError:
                nz3 = bot_z3
            self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                      nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)

            while not (round(bot_z3, 1) == 0.5 and round(bot_y3, 1) == -0.5):
                if round(bot_z3, 1) == 0.5:
                    up_y1 -= factor
                    up_y2 -= factor
                    up_y3 -= factor
                    bot_y1 -= factor
                    bot_y2 -= factor
                    bot_y3 -= factor

                    up_z1 = up_z1 + factor - 1
                    up_z2 = up_z2 + factor - 1
                    up_z3 = up_z3 + factor - 1
                    bot_z1 = bot_z1 + factor - 1
                    bot_z2 = bot_z2 + factor - 1
                    bot_z3 = bot_z3 + factor - 1
                else:
                    up_z1 += factor
                    up_z2 += factor
                    up_z3 += factor
                    bot_z1 += factor
                    bot_z2 += factor
                    bot_z3 += factor
                try:
                    nx1 = up_x1 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx1 = up_x1

                try:
                    nx2 = up_x2 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx2 = up_x2

                try:
                    nx3 = up_x3 / up_x1 + up_x2 + up_x3
                except ZeroDivisionError:
                    nx3 = up_x3

                try:
                    ny1 = up_y1 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny1 = up_y1

                try:
                    ny2 = up_y2 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny2 = up_y2

                try:
                    ny3 = up_y3 / up_y1 + up_y2 + up_y3
                except ZeroDivisionError:
                    ny3 = up_y3

                try:
                    nz1 = up_z1 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz1 = up_z1

                try:
                    nz2 = up_z2 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz2 = up_z2

                try:
                    nz3 = up_z3 / up_z1 + up_z2 + up_z3
                except ZeroDivisionError:
                    nz3 = up_z3
                self.addTriangleWithNorms(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3,
                                          nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
                try:
                    nx1 = bot_x1 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx1 = bot_x1

                try:
                    nx2 = bot_x2 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx2 = bot_x2

                try:
                    nx3 = bot_x3 / bot_x1 + bot_x2 + bot_x3
                except ZeroDivisionError:
                    nx3 = bot_x3

                try:
                    ny1 = bot_y1 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny1 = bot_y1

                try:
                    ny2 = bot_y2 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny2 = bot_y2

                try:
                    ny3 = bot_y3 / bot_y1 + bot_y2 + bot_y3
                except ZeroDivisionError:
                    ny3 = bot_y3

                try:
                    nz1 = bot_z1 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz1 = bot_z1

                try:
                    nz2 = bot_z2 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz2 = bot_z2

                try:
                    nz3 = bot_z3 / bot_z1 + bot_z2 + bot_z3
                except ZeroDivisionError:
                    nz3 = bot_z3
                self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3,
                                          nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)