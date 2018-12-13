'''
//  lamp.py
//
//  Routines for tessellating the cone of the lamp.
//
'''

from simpleShape import simpleShape
import math

class lamp(simpleShape):

    def __init__(self):
        pass

    def makeCone(self, radius, radialdivision, heightdivision):
        '''
        function to create polygons for a cone with unit height, centered at the origin,
        with separate number of radial subdivisions and height subdivisions
        :param radius: radius of the base of the cone
        :param radialdivision: number of subdivisions on the radial base
        :param heightdivision: number of subdivisions along the height
        '''

        if (radialdivision < 3):
            radialdivision = 3;

        if (heightdivision < 1):
            heightdivision = 1

        # add your implementation here

        # initializing the x, y, z coordinates for one triangle of the disk at one base of the cone
        # in the x-y plane when z = 0.5
        factor = 2 * math.pi / radialdivision
        disk_x1 = 0
        disk_y1 = 0
        disk_z1 = 0.5
        disk_x2 = radius
        disk_y2 = 0
        disk_z2 = 0.5
        disk_x3 = radius * math.cos(factor)
        disk_y3 = radius * math.sin(factor)
        disk_z3 = 0.5

        newfactor = factor

        # initializing the list to store the x and y coordinates of the disk at the base of the cone
        x_coords = []
        y_coords = []

        # interatively computing the coordinates of the successive triangles from the above triangle and drawing them,
        # given the number of subdivisions on the radial base, and storing the x and y coordinates in their lists
        for i in range(0, radialdivision):
            x_coords.append(disk_x3)
            y_coords.append(disk_y3)
            try:
                nx1 = disk_x1 / disk_x1 + disk_x2 + disk_x3
            except ZeroDivisionError:
                nx1 = disk_x1

            try:
                nx2 = disk_x2 / disk_x1 + disk_x2 + disk_x3
            except ZeroDivisionError:
                nx2 = disk_x2

            try:
                nx3 = disk_x3 / disk_x1 + disk_x2 + disk_x3
            except ZeroDivisionError:
                nx3 = disk_x3

            try:
                ny1 = disk_y1 / disk_y1 + disk_y2 + disk_y3
            except ZeroDivisionError:
                ny1 = disk_y1

            try:
                ny2 = disk_y2 / disk_y1 + disk_y2 + disk_y3
            except ZeroDivisionError:
                ny2 = disk_y2

            try:
                ny3 = disk_y3 / disk_y1 + disk_y2 + disk_y3
            except ZeroDivisionError:
                ny3 = disk_y3

            try:
                nz1 = disk_z1 / disk_z1 + disk_z2 + disk_z3
            except ZeroDivisionError:
                nz1 = disk_z1

            try:
                nz2 = disk_z2 / disk_z1 + disk_z2 + disk_z3
            except ZeroDivisionError:
                nz2 = disk_z2

            try:
                nz3 = disk_z3 / disk_z1 + disk_z2 + disk_z3
            except ZeroDivisionError:
                nz3 = disk_z3
            newfactor += factor
            disk_x2 = disk_x3
            disk_y2 = disk_y3
            if i == radialdivision - 2:
                disk_x3 = radius
                disk_y3 = 0
            else:
                disk_x3 = radius * math.cos(newfactor)
                disk_y3 = radius * math.sin(newfactor)

        # using the coordinates stored in the x and y lists, iteratively draw the triangles of the cone of
        # unit height, given the number of divisions along the height
        z_factor = 1.0 / heightdivision

        n = len(y_coords)

        x_new_coords = x_coords[:]
        y_new_coords = y_coords[:]

        x = x_coords[:]
        y = y_coords[:]

        z_new = 0.5
        for j in range(0, heightdivision):
            x_coords = x_new_coords[:]
            y_coords = y_new_coords[:]
            x_new_coords = []
            y_new_coords = []
            for i in range(1, n):
                if j <= heightdivision / 1.5:
                    # the x, y, and z coordinates of the upper (top) triangle in the rectangle
                    up_x1 = x_coords[i - 1]
                    up_y1 = y_coords[i - 1]
                    up_z1 = z_new
                    up_x2 = x[i - 1] + ((j + 1) * 1.0 / heightdivision) * (0 - x[i - 1])
                    up_y2 = y[i - 1] + ((j + 1) * 1.0 / heightdivision) * (0 - y[i - 1])
                    up_z2 = z_new - z_factor
                    up_x3 = x[i] + ((j + 1) * 1.0 / heightdivision) * (0 - x[i])
                    up_y3 = y[i] + ((j + 1) * 1.0 / heightdivision) * (0 - y[i])
                    up_z3 = z_new - z_factor

                    x_new_coords.append(up_x2)
                    y_new_coords.append(up_y2)

                    # the x, y, and z coordinates of the lower (bottom) triangle in the rectangle
                    bot_x1 = x[i] + ((j + 1) * 1.0 / heightdivision) * (0 - x[i])
                    bot_y1 = y[i] + ((j + 1) * 1.0 / heightdivision) * (0 - y[i])
                    bot_z1 = z_new - z_factor
                    bot_x2 = x_coords[i]
                    bot_y2 = y_coords[i]
                    bot_z2 = z_new
                    bot_x3 = x_coords[i - 1]
                    bot_y3 = y_coords[i - 1]
                    bot_z3 = z_new

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

                    if i == n - 1:
                        # draw the triangles of the final rectangle using the last and first coordinates in the x and y lists
                        up_x1 = x_coords[i]
                        up_y1 = y_coords[i]
                        up_z1 = z_new
                        up_x2 = x[i] + ((j + 1) * 1.0 / heightdivision) * (0 - x[i])
                        up_y2 = y[i] + ((j + 1) * 1.0 / heightdivision) * (0 - y[i])
                        up_z2 = z_new - z_factor
                        up_x3 = x[0] + ((j + 1) * 1.0 / heightdivision) * (0 - x[0])
                        up_y3 = y[0] + ((j + 1) * 1.0 / heightdivision) * (0 - y[0])
                        up_z3 = z_new - z_factor

                        x_new_coords.append(up_x2)
                        y_new_coords.append(up_y2)

                        bot_x1 = x[0] + ((j + 1) * 1.0 / heightdivision) * (0 - x[0])
                        bot_y1 = y[0] + ((j + 1) * 1.0 / heightdivision) * (0 - y[0])
                        bot_z1 = z_new - z_factor
                        bot_x2 = x_coords[0]
                        bot_y2 = y_coords[0]
                        bot_z2 = z_new
                        bot_x3 = x_coords[i]
                        bot_y3 = y_coords[i]
                        bot_z3 = z_new

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
                        self.addTriangleWithNorms(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3,
                                                  bot_z3,
                                                  nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)

                        z_new -= z_factor