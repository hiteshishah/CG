'''
Created on Aug 4, 2016

@author: Srinivas

Contributor:  Hiteshi Shah (hss7374)

Object for making four different shapes
'''
from math import cos, sin, radians
from numpy import arange,float32
from simpleShape import simpleShape
import math

class cgShape(simpleShape):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    #
    # makeCube - Create a unit cube, centered at the origin, with a given number
    # of subdivisions in each direction on each face.
    #
    # @param subdivision - number of equal subdivisions to be made in each
    #        direction along each face
    #
    # Can only use calls to addTriangle()
    #
    def makeCube(self,subdivisions):
        '''
        function to create a unit cube, centered at the origin, with a given number
        of subdivisions in each direction on each face
        :param subdivisions: the number of subdivisions in each direction on each face
        '''
        
        if(subdivisions < 1):
            subdivisions = 1

        #add your code here

        # initializing the co-ordinates for the face on the x-y plane when z = 0.5

        # the x, y, and z co-ordinates of the upper (top) triangle of the square
        up_x1 = -0.5
        up_y1 = 0.5
        up_z1 = 0.5
        up_x2 = -0.5
        up_y2 = -0.5
        up_z2 = 0.5
        up_x3 = 0.5
        up_y3 = 0.5
        up_z3 = 0.5

        # the x, y, and z co-ordinates of the lower (bottom) triangle of the square
        bot_x1 = 0.5
        bot_y1 = 0.5
        bot_z1 = 0.5
        bot_x2 = -0.5
        bot_y2 = -0.5
        bot_z2 = 0.5
        bot_x3 = 0.5
        bot_y3 = -0.5
        bot_z3 = 0.5

        # if the number of subdivisions is 1, draw the triangles
        if subdivisions == 1:
            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)
        # if the number of subdivisions is more than 1, iteratively divide the face into smaller triangles
        else:
            factor = abs(up_x1 - up_x3) / subdivisions

            up_y2 = up_y1 - factor
            up_x3 = up_x1 + factor

            bot_x1 = up_x3
            bot_y2 = up_y2
            bot_x3 = bot_x2 + factor
            bot_y3 = bot_y1 - factor

            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

            while not (round(bot_x3,1) == 0.5 and round(bot_y3, 1) == -0.5):
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
                    up_x3 +=  factor
                    bot_x1 += factor
                    bot_x2 += factor
                    bot_x3 += factor
                self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
                self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

        # initializing the co-ordinates for the face on the x-y plane when z = -0.5

        # the x, y, and z co-ordinates of the upper (top) triangle of the square
        up_x1 = -0.5
        up_y1 = -0.5
        up_z1 = -0.5
        up_x2 = -0.5
        up_y2 = 0.5
        up_z2 = -0.5
        up_x3 = 0.5
        up_y3 = -0.5
        up_z3 = -0.5

        # the x, y, and z co-ordinates of the lower (bottom) triangle of the square
        bot_x1 = 0.5
        bot_y1 = -0.5
        bot_z1 = -0.5
        bot_x2 = -0.5
        bot_y2 = 0.5
        bot_z2 = -0.5
        bot_x3 = 0.5
        bot_y3 = 0.5
        bot_z3 = -0.5

        # if the number of subdivisions is 1, draw the triangles
        if subdivisions == 1:
            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)
        # if the number of subdivisions is more than 1, iteratively divide the face into smaller triangles
        else:
            factor = abs(up_x1 - up_x3) / subdivisions

            up_y2 = up_y1 + factor
            up_x3 = up_x1 + factor

            bot_x1 = up_x3
            bot_y2 = up_y2
            bot_x3 = bot_x2 + factor
            bot_y3 = bot_y1 + factor

            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

            while not (round(bot_x3, 1) == 0.5 and round(bot_y3, 1) == 0.5):
                if round(bot_x3, 1) == 0.5:
                    up_y1 += factor
                    up_y2 += factor
                    up_y3 += factor
                    bot_y1 += factor
                    bot_y2 += factor
                    bot_y3 += factor

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
                self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
                self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

        # initializing the co-ordinates for the face on the x-z plane when y = 0.5

        # the x, y, and z co-ordinates of the upper (top) triangle of the square
        up_x1 = -0.5
        up_y1 = 0.5
        up_z1 = -0.5
        up_x2 = -0.5
        up_y2 = 0.5
        up_z2 = 0.5
        up_x3 = 0.5
        up_y3 = 0.5
        up_z3 = -0.5

        # the x, y, and z co-ordinates of the lower (bottom) triangle of the square
        bot_x1 = 0.5
        bot_y1 = 0.5
        bot_z1 = -0.5
        bot_x2 = -0.5
        bot_y2 = 0.5
        bot_z2 = 0.5
        bot_x3 = 0.5
        bot_y3 = 0.5
        bot_z3 = 0.5

        # if the number of subdivisions is 1, draw the triangles
        if subdivisions == 1:
            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)
        # if the number of subdivisions is more than 1, iteratively divide the face into smaller triangles
        else:
            factor = abs(up_x1 - up_x3) / subdivisions

            up_z2 = up_z1 + factor
            up_x3 = up_x1 + factor

            bot_x1 = up_x3
            bot_z2 = up_z2
            bot_x3 = bot_x2 + factor
            bot_z3 = bot_z1 + factor

            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

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
                self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
                self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

        # initializing the co-ordinates for the face on the x-z plane when y = -0.5

        # the x, y, and z co-ordinates of the upper (top) triangle of the square
        up_x1 = -0.5
        up_y1 = -0.5
        up_z1 = 0.5
        up_x2 = -0.5
        up_y2 = -0.5
        up_z2 = -0.5
        up_x3 = 0.5
        up_y3 = -0.5
        up_z3 = 0.5

        # the x, y, and z co-ordinates of the lower (bottom) triangle of the square
        bot_x1 = 0.5
        bot_y1 = -0.5
        bot_z1 = 0.5
        bot_x2 = -0.5
        bot_y2 = -0.5
        bot_z2 = -0.5
        bot_x3 = 0.5
        bot_y3 = -0.5
        bot_z3 = -0.5

        # if the number of subdivisions is 1, draw the triangles
        if subdivisions == 1:
            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)
        # if the number of subdivisions is more than 1, iteratively divide the face into smaller triangles
        else:
            factor = abs(up_x1 - up_x3) / subdivisions

            up_z2 = up_z1 - factor
            up_x3 = up_x1 + factor

            bot_x1 = up_x3
            bot_z2 = up_z2
            bot_x3 = bot_x2 + factor
            bot_z3 = bot_z1 - factor

            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

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
                self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
                self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

        # initializing the co-ordinates for the face on the y-z plane when x = -0.5

        # the x, y, and z co-ordinates of the upper (top) triangle of the square
        up_x1 = -0.5
        up_y1 = 0.5
        up_z1 = -0.5
        up_x2 = -0.5
        up_y2 = -0.5
        up_z2 = -0.5
        up_x3 = -0.5
        up_y3 = 0.5
        up_z3 = 0.5

        # the x, y, and z co-ordinates of the lower (bottom) triangle of the square
        bot_x1 = -0.5
        bot_y1 = 0.5
        bot_z1 = 0.5
        bot_x2 = -0.5
        bot_y2 = -0.5
        bot_z2 = -0.5
        bot_x3 = -0.5
        bot_y3 = -0.5
        bot_z3 = 0.5

        # if the number of subdivisions is 1, draw the triangles
        if subdivisions == 1:
            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)
        # if the number of subdivisions is more than 1, iteratively divide the face into smaller triangles
        else:
            factor = abs(up_z1 - up_z3) / subdivisions

            up_y2 = up_y1 - factor
            up_z3 = up_z1 + factor

            bot_z1 = up_z3
            bot_y2 = up_y2
            bot_z3 = bot_z2 + factor
            bot_y3 = bot_y1 - factor

            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

            while not (round(bot_z3,1) == 0.5 and round(bot_y3, 1) == -0.5):
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
                    up_z3 +=  factor
                    bot_z1 += factor
                    bot_z2 += factor
                    bot_z3 += factor
                self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
                self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

        # initializing the co-ordinates for the face on the y-z plane when x = 0.5

        # the x, y, and z co-ordinates of the upper (top) triangle of the square
        up_x1 = 0.5
        up_y1 = -0.5
        up_z1 = -0.5
        up_x2 = 0.5
        up_y2 = 0.5
        up_z2 = -0.5
        up_x3 = 0.5
        up_y3 = -0.5
        up_z3 = 0.5

        # the x, y, and z co-ordinates of the lower (bottom) triangle of the square
        bot_x1 = 0.5
        bot_y1 = -0.5
        bot_z1 = 0.5
        bot_x2 = 0.5
        bot_y2 = 0.5
        bot_z2 = -0.5
        bot_x3 = 0.5
        bot_y3 = 0.5
        bot_z3 = 0.5

        # if the number of subdivisions is 1, draw the triangles
        if subdivisions == 1:
            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)
        # if the number of subdivisions is more than 1, iteratively divide the face into smaller triangles
        else:
            factor = abs(up_z1 - up_z3) / subdivisions

            up_y2 = up_y1 + factor
            up_z3 = up_z1 + factor

            bot_z1 = up_z3
            bot_y2 = up_y2
            bot_z3 = bot_z2 + factor
            bot_y3 = bot_y1 + factor

            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

            while not (round(bot_z3, 1) == 0.5 and round(bot_y3, 1) == 0.5):
                if round(bot_z3, 1) == 0.5:
                    up_y1 += factor
                    up_y2 += factor
                    up_y3 += factor
                    bot_y1 += factor
                    bot_y2 += factor
                    bot_y3 += factor

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
                self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
                self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)
        
    #
    # makeCylinder - Create polygons for a cylinder with unit height, centered at
    # the origin, with separate number of radial subdivisions and height
    # subdivisions.
    #
    # @param radius - Radius of the base of the cylinder
    # @param radialDivision - number of subdivisions on the radial base
    # @param heightDivisions - number of subdivisions along the height
    #
    # Can only use calls to addTriangle()
    #
    def makeCylinder(self,radius,radialdivision,heightdivision):
        '''
        function to create polygons for a cylinder with unit height, centered at the origin,
        with separate number of radial subdivisions and height subdivisions.
        :param radius: radius of the base of the cylinder
        :param radialdivision: number of subdivisions on the radial base
        :param heightdivision: number of subdivisions along the height
        '''

        if(radialdivision < 3):
            radialdivision = 3;
            
        if(heightdivision < 1):
            heightdivision = 1

        #add your code here

        # initializing the x, y, z coordinates for one triangle of the disk at one base of the cylinder
        # in the x-z plane when y = 0.5
        factor = 2 * math.pi / radialdivision
        disk_x1 = 0
        disk_y1 = 0.5
        disk_z1 = 0
        disk_x2 = radius
        disk_y2 = 0.5
        disk_z2 = 0
        disk_x3 = radius * cos(factor)
        disk_y3 = 0.5
        disk_z3 = -1 * radius * sin(factor)

        newfactor = factor

        # initializing the list to store the x and z coordinates of the disk at the base of the cylinder
        x_coords = []
        z_coords = []

        # interatively computing the coordinates of the successive triangles from the above triangle and drawing them,
        # given the number of subdivisions on the radial base, and storing the x and z coordinates in their lists
        for i in range(0, radialdivision):
            x_coords.append(disk_x3)
            z_coords.append(disk_z3)
            self.addTriangle(disk_x1, disk_y1, disk_z1, disk_x2, disk_y2, disk_z2, disk_x3, disk_y3, disk_z3)
            newfactor += factor
            disk_x2 = disk_x3
            disk_z2 = disk_z3
            if i == radialdivision - 2:
                disk_x3 = radius
                disk_z3 = 0
            else:
                disk_x3 = radius * cos(newfactor)
                disk_z3 = -1 * radius * sin(newfactor)

        # initializing the x, y, z coordinates for one triangle of the disk at the other base of the cylinder
        # in the x-z plane when y = -0.5
        disk_x1 = 0
        disk_y1 = -0.5
        disk_z1 = 0
        disk_x2 = radius
        disk_y2 = -0.5
        disk_z2 = 0
        disk_x3 = radius * cos(factor)
        disk_y3 = -0.5
        disk_z3 = radius * sin(factor)

        newfactor = factor

        # interatively computing the coordinates of the successive triangles from the above triangle and drawing them,
        # given the number of subdivisions on the radial base
        for i in range(0, radialdivision):
            self.addTriangle(disk_x1, disk_y1, disk_z1, disk_x2, disk_y2, disk_z2, disk_x3, disk_y3, disk_z3)
            newfactor += factor
            disk_x2 = disk_x3
            disk_z2 = disk_z3
            if i == radialdivision - 2:
                disk_x3 = radius
                disk_z3 = 0
            else:
                disk_x3 = radius * cos(newfactor)
                disk_z3 = radius * sin(newfactor)

        # using the coordinates stored in the x and z lists, iteratively draw the triangles of the cylinder of
        # unit height, given the number of divisions along the height
        factor = 1.0 / heightdivision

        n = len(z_coords)

        for i in range(1, n):
            y_new = 0.5
            for j in range(0, heightdivision):
                # the x, y, and z coordinates of the upper (top) triangle in the rectangle
                up_x1 = x_coords[i - 1]
                up_y1 = y_new
                up_z1 = z_coords[i - 1]
                up_x2 = x_coords[i - 1]
                up_y2 = y_new - factor
                up_z2 = z_coords[i - 1]
                up_x3 = x_coords[i]
                up_y3 = y_new - factor
                up_z3 = z_coords[i]

                # the x, y, and z coordinates of the lower (bottom) triangle in the rectangle
                bot_x1 = x_coords[i]
                bot_y1 = y_new - factor
                bot_z1 = z_coords[i]
                bot_x2 = x_coords[i]
                bot_y2 = y_new
                bot_z2 = z_coords[i]
                bot_x3 = x_coords[i - 1]
                bot_y3 = y_new
                bot_z3 = z_coords[i - 1]

                self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
                self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

                y_new -= factor

        # draw the triangles of the final rectangle using the last and first coordinates in the x and z lists
        y_new = 0.5
        for j in range(0, heightdivision):
            up_x1 = x_coords[n - 1]
            up_y1 = y_new
            up_z1 = z_coords[n - 1]
            up_x2 = x_coords[n - 1]
            up_y2 = y_new - factor
            up_z2 = z_coords[n - 1]
            up_x3 = x_coords[0]
            up_y3 = y_new - factor
            up_z3 = z_coords[0]

            bot_x1 = x_coords[0]
            bot_y1 = y_new - factor
            bot_z1 = z_coords[0]
            bot_x2 = x_coords[0]
            bot_y2 = y_new
            bot_z2 = z_coords[0]
            bot_x3 = x_coords[n - 1]
            bot_y3 = y_new
            bot_z3 = z_coords[n - 1]

            self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
            self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

            y_new -= factor

    #
    # makeCone - Create polygons for a cone with unit height, centered at the
    # origin, with separate number of radial subdivisions and height
    # subdivisions.
    #
    # @param radius - Radius of the base of the cone
    # @param radialDivision - number of subdivisions on the radial base
    # @param heightDivisions - number of subdivisions along the height
    #
    # Can only use calls to addTriangle()
    #
    def makeCone(self, radius, radialdivision, heightdivision):
        '''
        function to create polygons for a cone with unit height, centered at the origin,
        with separate number of radial subdivisions and height subdivisions
        :param radius: radius of the base of the cone
        :param radialdivision: number of subdivisions on the radial base
        :param heightdivision: number of subdivisions along the height
        '''

        if(radialdivision < 3):
            radialdivision = 3;
            
        if(heightdivision < 1):
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
        disk_x3 = radius * cos(factor)
        disk_y3 = radius * sin(factor)
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
            self.addTriangle(disk_x1, disk_y1, disk_z1, disk_x2, disk_y2, disk_z2, disk_x3, disk_y3, disk_z3)
            newfactor += factor
            disk_x2 = disk_x3
            disk_y2 = disk_y3
            if i == radialdivision - 2:
                disk_x3 = radius
                disk_y3 = 0
            else:
                disk_x3 = radius * cos(newfactor)
                disk_y3 = radius * sin(newfactor)

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
                if j == heightdivision - 1:
                    # if we're only one heightsubdivision away from the tip of the cone,
                    # we only need to draw one set of triangles
                    up_x1 = x_coords[i - 1]
                    up_y1 = -1 * y_coords[i - 1]
                    up_z1 = z_new
                    up_x2 = x_coords[i]
                    up_y2 = -1 * y_coords[i]
                    up_z2 = z_new
                    up_x3 = 0
                    up_y3 = 0
                    up_z3 = z_new - z_factor

                    self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)

                    if i == n - 1:
                        # draw the triangle using the last and first coordinates in the x and y lists
                        up_x1 = x_coords[i]
                        up_y1 = -1 * y_coords[i]
                        up_z1 = z_new
                        up_x2 = x_coords[0]
                        up_y2 = -1 * y_coords[0]
                        up_z2 = z_new
                        up_x3 = 0
                        up_y3 = 0
                        up_z3 = z_new - z_factor

                        self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)

                else:
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

                    self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
                    self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

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

                        self.addTriangle(up_x1, up_y1, up_z1, up_x2, up_y2, up_z2, up_x3, up_y3, up_z3)
                        self.addTriangle(bot_x1, bot_y1, bot_z1, bot_x2, bot_y2, bot_z2, bot_x3, bot_y3, bot_z3)

                        z_new -= z_factor

    #
    # makeSphere - Create sphere of a given radius, centered at the origin,
    # using spherical coordinates with separate number of thetha and
    # phi subdivisions.
    #
    # @param radius - Radius of the sphere
    # @param slices 3- number of subdivisions in the theta direction
    # @param stacks - Number of subdivisions in the phi direction.
    #
    # Can only use calls to addTriangle()
    #
    def makeSphere(self,radius, slices, stacks):
        '''
        function to create sphere of a given radius, centered at the origin, using spherical coordinates with separate
        number of thetha and phi subdivisions
        :param radius: radius of the sphere
        :param slices: number of subdivisions in the theta direction
        :param stacks: number of subdivisions in the phi direction
        :return:
        '''
    
        # IF DOING RECURSIVE SUBDIVISION:
        # use a minimum value of 1 instead of 3
        # add an 'else' clause to set a maximum value of 5
        if(slices < 1):
            slices = 1
        elif (slices > 5):
            slices = 5

        if(stacks < 3):
            stacks = 3
        
        # add your implementation here.

        # following the geometric description given in the slides of an icosahedron,
        # we get the following vertices in the list v
        a = 2.0 / (1 + math.sqrt(5))
        v = []
        v.append([0, a, -1])
        v.append([-a, 1, 0])
        v.append([a, 1, 0])
        v.append([0, a, 1])
        v.append([-1, 0, a])
        v.append([0, -a, 1])
        v.append([1, 0, a])
        v.append([1, 0, -a])
        v.append([0, -a, -1])
        v.append([-1, 0, -a])
        v.append([-a, -1, 0])
        v.append([a, -1, 0])

        # calling the recursive function on each of the triangles of the icosahedron as given in the slide
        self.subdivide(v[0][0], v[0][1], v[0][2], v[1][0], v[1][1], v[1][2], v[2][0], v[2][1], v[2][2], slices, radius)
        self.subdivide(v[3][0], v[3][1], v[3][2], v[2][0], v[2][1], v[2][2], v[1][0], v[1][1], v[1][2], slices, radius)
        self.subdivide(v[3][0], v[3][1], v[3][2], v[4][0], v[4][1], v[4][2], v[5][0], v[5][1], v[5][2], slices, radius)
        self.subdivide(v[3][0], v[3][1], v[3][2], v[5][0], v[5][1], v[5][2], v[6][0], v[6][1], v[6][2], slices, radius)
        self.subdivide(v[0][0], v[0][1], v[0][2], v[7][0], v[7][1], v[7][2], v[8][0], v[8][1], v[8][2], slices, radius)
        self.subdivide(v[0][0], v[0][1], v[0][2], v[8][0], v[8][1], v[8][2], v[9][0], v[9][1], v[9][2], slices, radius)
        self.subdivide(v[5][0], v[5][1], v[5][2], v[10][0], v[10][1], v[10][2], v[11][0], v[11][1], v[11][2], slices, radius)
        self.subdivide(v[8][0], v[8][1], v[8][2], v[11][0], v[11][1], v[11][2], v[10][0], v[10][1], v[10][2], slices, radius)
        self.subdivide(v[1][0], v[1][1], v[1][2], v[9][0], v[9][1], v[9][2], v[4][0], v[4][1], v[4][2], slices, radius)
        self.subdivide(v[10][0], v[10][1], v[10][2], v[4][0], v[4][1], v[4][2], v[9][0], v[9][1], v[9][2], slices, radius)
        self.subdivide(v[2][0], v[2][1], v[2][2], v[6][0], v[6][1], v[6][2], v[7][0], v[7][1], v[7][2], slices, radius)
        self.subdivide(v[11][0], v[11][1], v[11][2], v[7][0], v[7][1], v[7][2], v[6][0], v[6][1], v[6][2], slices, radius)
        self.subdivide(v[3][0], v[3][1], v[3][2], v[1][0], v[1][1], v[1][2], v[4][0], v[4][1], v[4][2], slices, radius)
        self.subdivide(v[3][0], v[3][1], v[3][2], v[6][0], v[6][1], v[6][2], v[2][0], v[2][1], v[2][2], slices, radius)
        self.subdivide(v[0][0], v[0][1], v[0][2], v[9][0], v[9][1], v[9][2], v[1][0], v[1][1], v[1][2], slices, radius)
        self.subdivide(v[0][0], v[0][1], v[0][2], v[2][0], v[2][1], v[2][2], v[7][0], v[7][1], v[7][2], slices, radius)
        self.subdivide(v[8][0], v[8][1], v[8][2], v[10][0], v[10][1], v[10][2], v[9][0], v[9][1], v[9][2], slices, radius)
        self.subdivide(v[8][0], v[8][1], v[8][2], v[7][0], v[7][1], v[7][2], v[11][0], v[11][1], v[11][2], slices, radius)
        self.subdivide(v[5][0], v[5][1], v[5][2], v[4][0], v[4][1], v[4][2], v[10][0], v[10][1], v[10][2], slices, radius)
        self.subdivide(v[5][0], v[5][1], v[5][2], v[11][0], v[11][1], v[11][2], v[6][0], v[6][1], v[6][2], slices, radius)


    def subdivide(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, slices, radius):
        '''
        function to recursively subdivide and normalize each side of the icosahedron depending on the
        number of subdivisions in the theta direction
        :param x1: x coordinate of vertex 1 of the triangle
        :param y1: y coordinate of vertex 1 of the triangle
        :param z1: z coordinate of vertex 1 of the triangle
        :param x2: x coordinate of vertex 2 of the triangle
        :param y2: y coordinate of vertex 2 of the triangle
        :param z2: z coordinate of vertex 2 of the triangle
        :param x3: x coordinate of vertex 3 of the triangle
        :param y3: y coordinate of vertex 3 of the triangle
        :param z3: z coordinate of vertex 3 of the triangle
        :param slices: number of subdivisions in the theta direction
        :param radius: radius of the sphere
        :return:
        '''
        if slices == 1:
            # if the number of subdivisions in the theta direction is 1, we normalize each of the vertices of the
            # triangle and scale them to the radius

            s = 1.0 / math.sqrt(math.pow(x1, 2) + math.pow(y1, 2) + math.pow(z1, 2))
            x1 *= s
            y1 *= s
            z1 *= s
            s = 1.0 / math.sqrt(math.pow(x2, 2) + math.pow(y2, 2) + math.pow(z2, 2))
            x2 *= s
            y2 *= s
            z2 *= s
            s = 1.0 / math.sqrt(math.pow(x3, 2) + math.pow(y3, 2) + math.pow(z3, 2))
            x3 *= s
            y3 *= s
            z3 *= s
            self.addTriangle(x1 * radius, y1 * radius, z1 * radius, x2 * radius, y2 * radius, z2 * radius, x3 * radius, y3 * radius, z3 * radius)
        else:
            # if the number of subdivisions in the theta direction is more than 1, we calculate the midpoints of each
            # side of the triangle and normalize them

            x12 = 0.5 * (x1 + x2)
            y12 = 0.5 * (y1 + y2)
            z12 = 0.5 * (z1 + z2)
            s = 1.0 / math.sqrt(math.pow(x12, 2) + math.pow(y12, 2) + math.pow(z12, 2))
            x12 *= s
            y12 *= s
            z12 *= s

            x13 = 0.5 * (x1 + x3)
            y13 = 0.5 * (y1 + y3)
            z13 = 0.5 * (z1 + z3)
            s = 1.0 / math.sqrt(math.pow(x13, 2) + math.pow(y13, 2) + math.pow(z13, 2))
            x13 *= s
            y13 *= s
            z13 *= s

            x23 = 0.5 * (x2 + x3)
            y23 = 0.5 * (y2 + y3)
            z23 = 0.5 * (z2 + z3)
            s = 1.0 / math.sqrt(math.pow(x23, 2) + math.pow(y23, 2) + math.pow(z23, 2))
            x23 *= s
            y23 *= s
            z23 *= s

            # recusive calls to the subdivide function using the newly computed midpoints and passing the number of
            # subdivisions in the theta direction reduced by one
            self.subdivide(x1, y1, z1, x12, y12, z12, x13, y13, z13, slices - 1, radius)
            self.subdivide(x12, y12, z12, x2, y2, z2, x23, y23, z23, slices - 1, radius)
            self.subdivide(x13, y13, z13, x23, y23, z23, x3, y3, z3, slices - 1, radius)
            self.subdivide(x12, y12, z12, x23, y23, z23, x13, y13, z13, slices - 1, radius)