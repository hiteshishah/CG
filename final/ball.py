'''
//  ball.py
//
//  Routines for tessellating a standard ball.
//
'''

from simpleShape import simpleShape
import math

class ball(simpleShape):

    def __init__(self):
        pass

    def makeSphere(self, radius, slices, stacks):
        '''
        function to create sphere of a given radius, centered at the origin, using spherical coordinates with separate
        number of thetha and phi subdivisions
        :param radius: radius of the sphere
        :param slices: number of subdivisions in the theta direction
        :param stacks: number of subdivisions in the phi direction
        :return:
        '''

        if (slices < 1):
            slices = 1
        elif (slices > 5):
            slices = 5

        if (stacks < 3):
            stacks = 3

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
        self.subdivide(v[5][0], v[5][1], v[5][2], v[10][0], v[10][1], v[10][2], v[11][0], v[11][1], v[11][2], slices,
                       radius)
        self.subdivide(v[8][0], v[8][1], v[8][2], v[11][0], v[11][1], v[11][2], v[10][0], v[10][1], v[10][2], slices,
                       radius)
        self.subdivide(v[1][0], v[1][1], v[1][2], v[9][0], v[9][1], v[9][2], v[4][0], v[4][1], v[4][2], slices, radius)
        self.subdivide(v[10][0], v[10][1], v[10][2], v[4][0], v[4][1], v[4][2], v[9][0], v[9][1], v[9][2], slices,
                       radius)
        self.subdivide(v[2][0], v[2][1], v[2][2], v[6][0], v[6][1], v[6][2], v[7][0], v[7][1], v[7][2], slices, radius)
        self.subdivide(v[11][0], v[11][1], v[11][2], v[7][0], v[7][1], v[7][2], v[6][0], v[6][1], v[6][2], slices,
                       radius)
        self.subdivide(v[3][0], v[3][1], v[3][2], v[1][0], v[1][1], v[1][2], v[4][0], v[4][1], v[4][2], slices, radius)
        self.subdivide(v[3][0], v[3][1], v[3][2], v[6][0], v[6][1], v[6][2], v[2][0], v[2][1], v[2][2], slices, radius)
        self.subdivide(v[0][0], v[0][1], v[0][2], v[9][0], v[9][1], v[9][2], v[1][0], v[1][1], v[1][2], slices, radius)
        self.subdivide(v[0][0], v[0][1], v[0][2], v[2][0], v[2][1], v[2][2], v[7][0], v[7][1], v[7][2], slices, radius)
        self.subdivide(v[8][0], v[8][1], v[8][2], v[10][0], v[10][1], v[10][2], v[9][0], v[9][1], v[9][2], slices,
                       radius)
        self.subdivide(v[8][0], v[8][1], v[8][2], v[7][0], v[7][1], v[7][2], v[11][0], v[11][1], v[11][2], slices,
                       radius)
        self.subdivide(v[5][0], v[5][1], v[5][2], v[4][0], v[4][1], v[4][2], v[10][0], v[10][1], v[10][2], slices,
                       radius)
        self.subdivide(v[5][0], v[5][1], v[5][2], v[11][0], v[11][1], v[11][2], v[6][0], v[6][1], v[6][2], slices,
                       radius)

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

            try:
                nx1 = x1 / x1 + x2 + x3
            except ZeroDivisionError:
                nx1 = x1

            try:
                nx2 = x2 / x1 + x2 + x3
            except ZeroDivisionError:
                nx2 = x2

            try:
                nx3 = x3 / x1 + x2 + x3
            except ZeroDivisionError:
                nx3 = x3

            try:
                ny1 = y1 / y1 + y2 + y3
            except ZeroDivisionError:
                ny1 = y1

            try:
                ny2 = y2 / y1 + y2 + y3
            except ZeroDivisionError:
                ny2 = y2

            try:
                ny3 = y3 / y1 + y2 + y3
            except ZeroDivisionError:
                ny3 = y3

            try:
                nz1 = z1 / z1 + z2 + z3
            except ZeroDivisionError:
                nz1 = z1

            try:
                nz2 = z2 / z1 + z2 + z3
            except ZeroDivisionError:
                nz2 = z2

            try:
                nz3 = z3 / z1 + z2 + z3
            except ZeroDivisionError:
                nz3 = z3

            self.addTriangleWithNorms(x1 * radius, y1 * radius, z1 * radius, x2 * radius, y2 * radius, z2 * radius, x3 * radius,
                             y3 * radius, z3 * radius, nx1, ny1, nz1, nx2, ny2, nz2, nx3, ny3, nz3)
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