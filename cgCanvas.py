# cgCanvas.py
#
# Contributor:  Hiteshi Shah (hss7374)
#
# Object for implementing the 2D pipeline

from simpleCanvas import simpleCanvas
from clipper import clipper
import numpy as np
import math

class cgCanvas(simpleCanvas):

    clipperObj = None

    def __init__(self,w,h):
        self.index = -1                 # initializing the unique ID for the polygons
        self.polygons = {}              # initializing the dictionary to hold the polygon IDs along with their vertices
        self.setSize(w,h)
        self.clipperObj = clipper()     # creating an object of the clipper class

        # initializing the global transformation matrix to be the identity matrix
        self.currentTransformation = np.array([[1, 0, 0],
                                               [0, 1, 0],
                                               [0, 0, 1]], dtype='f')
        self.bottom = -1                # initializing the y coord of bottom edge of the clip window
        self.top = -1                   # initializing the y coord of top edge of the clip window
        self.right = -1                 # initializing the x coord of right edge of the clip window
        self.left = -1                  # initialzing the x coord of the left edge of the clip window

        # initializing the viewport transformation matrix to be the identity matrix
        self.viewTransform = np.array([[1, 0, 0],
                                       [0, 1, 0],
                                       [0, 0, 1]], dtype='f')

    '''
    *
    * addPoly - Adds and stores a polygon to the canvas.  Note that this method does not
    *           draw the polygon, but merely stores it for later draw.  Drawing is
    *           initiated by the draw() method.
    *
    *           Returns a unique integer id for the polygon.
    *
    * @param x - Array of x coords of the vertices of the polygon to be added.
    * @param y - Array of y coords of the vertices of the polygin to be added.
    * @param n - Number of verticies in polygon
    *
    * @return a unique integer identifier for the polygon
    '''
    def addPoly(self,x,y,n):
        '''
        function that adds and stores a polygon to the canvas
        :param x: list of x coords of the vertices of the polygon to be added.
        :param y: list of y coords of the vertices of the polygon to be added.
        :param n: no. of vertices in polygon
        :return: a unique integer identifier for the polygon
        '''
        self.index += 1
        x_new = [i for i in x if i != None]
        y_new = [i for i in y if i != None]
        self.polygons[self.index] = [x_new, y_new, n]

        return self.index

    '''
     *
     * clearTransform - sets the current transformation to be the identity
     *
    '''
    def clearTransform(self):
        '''
        function to set the current transformation to be the identity
        '''
        self.currentTransformation[0, 0] = 1
        self.currentTransformation[0, 1] = 0
        self.currentTransformation[0, 2] = 0
        self.currentTransformation[1, 0] = 0
        self.currentTransformation[1, 1] = 1
        self.currentTransformation[1, 2] = 0
        self.currentTransformation[2, 0] = 0
        self.currentTransformation[2, 1] = 0
        self.currentTransformation[2, 2] = 1


    def createEdgeTable(self, n, x, y):
        '''
        function to create the edge table, given the number of vertices and the lists of x- and y-coordinates
        :param n: number of vertices
        :param x: list of x-coordinates
        :param y: list of y-coordinates
        :return: returns the final table containing all the edges of the polygon
        '''
        edge_table = []                 # initializing the edge table

        # adding the edge from vertex n -1 to vertex 0 to the table
        if (y[n - 1] - y[0]) != 0:      # making sure the edge isn't horizontal
            # finding out the indices with the min and max x-values of the edge
            if x[n - 1] < x[0]:
                xmin = n - 1
                xmax = 0
            else:
                xmin = 0
                xmax = n - 1
            dx = x[xmin] - x[xmax]
            dy = y[xmin] - y[xmax]
            # finding out the indices with the min and max y-values of the edge
            if y[n - 1] < y[0]:
                ymin = n - 1
                ymax = 0
            else:
                ymin = 0
                ymax = n - 1
            bucket = [y[ymin], y[ymax], x[ymin], dx, dy, 0]
            edge_table.append(bucket)

        # processing all the other pairs of edges from vertices 0 to n - 1 and adding them to the table
        for i in range(1, n):
            if y[i - 1] - y[i] != 0:    # making sure the edge isn't horizontal
                # finding out the indices with the min and max x-values of the edge
                if x[i - 1] < x[i]:
                    xmin = i - 1
                    xmax = i
                else:
                    xmin = i
                    xmax = i - 1
                dx = x[xmin] - x[xmax]
                dy = y[xmin] - y[xmax]
                # finding out the indices with the min and max y-values of the edge
                if y[i - 1] < y[i]:
                    ymin = i - 1
                    ymax = i
                else:
                    ymin = i
                    ymax = i - 1
                bucket = [y[ymin], y[ymax], x[ymin], dx, dy, 0]
                edge_table.append(bucket)

        return edge_table

    '''
     *
     * draw - Draw the polygon with the given id.  Draw should draw the polygon after applying the
     *        current transformation on the vertices of the polygon.
     *
     * @param polyID - the ID of the polygin to be drawn.
    '''
    def drawPoly(self, polyID):
        '''
        function that draws the polygon with the given id, having gone through the entire 2D pipeline
        :param polyID: the ID of the polygon to be drawn
        '''
        polygon = self.polygons[polyID]

        new_polygonx = []
        new_polygony = []

        # applying the transformation matrix to the polygon
        for i in range(0, polygon[2]):
            p = np.array([polygon[0][i], polygon[1][i], 1])
            new_p = self.currentTransformation.dot(p)
            new_polygonx.append(new_p[0])
            new_polygony.append(new_p[1])

        outx = []
        outy = []

        # clipping the polygon against the clip window
        n = self.clipperObj.clipPolygon(len(new_polygonx), new_polygonx, new_polygony, outx, outy,
                                        self.left, self.bottom, self.right, self.top)

        new_polygonx = []
        new_polygony = []

        # setting the viewport for the polygon to be drawn in
        for i in range(0, len(outx)):
            p = np.array([outx[i], outy[i], 1])
            new_p = self.viewTransform.dot(p)
            new_polygonx.append(int(new_p[0]))
            new_polygony.append(int(new_p[1]))

        edge_table = self.createEdgeTable(len(new_polygonx), new_polygonx, new_polygony)

        # sorting the edge table based on y-min in ascending order
        edge_table = sorted(edge_table, key=lambda a: a[0])

        # initializing scan line to the smallest y-min
        scan_line = edge_table[0][0]

        # initializing the active list
        active_list = []

        while len(edge_table) != 0:
            # removing edges from the active list if y = ymax
            if len(active_list) != 0:
                index = len(active_list) - 1
                while index >= 0:
                    if active_list[index][1] == scan_line:
                        edge_removed = active_list.pop(index)
                        edge_table.remove(edge_removed)
                    index -= 1

            # adding the edge from the edge table to the active list if y = ymin
            for bucket in edge_table:
                if bucket[0] == scan_line:
                    active_list.append(bucket)

            # sorting the active list by x position in ascending order
            active_list = sorted(active_list, key=lambda a: a[2])

            # filling the polygon for the current scan line
            for edge in range(1, len(active_list), 2):
                for x in range(int(active_list[edge - 1][2]), int(active_list[edge][2])):
                    super(cgCanvas, self).setPixel(x, scan_line)

            # incrementing the scan line
            scan_line += 1

            # incrementing or decrementing x of each bucket in the active list based on their slopes
            for bucket in active_list:
                if abs(bucket[3]) != 0:
                    bucket[5] += abs(bucket[3])

                while bucket[5] >= abs(bucket[4]):
                    if (bucket[4] > 0 and bucket[3] < 0) or (bucket[3] > 0 and bucket[4] < 0):
                        bucket[2] -= 1
                    else:
                        bucket[2] += 1
                    bucket[5] -= abs(bucket[4])


    '''
     *
     * rotate - Add a rotation to the current transformation by premultiplying the appropriate
     *          rotation matrix to the current transformtion matrix.
     *
     * @param degrees - Amount of rotation in degrees.
     *
    '''
    def rotate(self, degrees):
        '''
        function that adds a rotation to the current transformation by pre-multiplying the
        rotation matrix to the current transformation matrix
        :param degrees: amount of rotation in degrees
        '''
        r = np.array([[math.cos(math.radians(degrees)), -math.sin(math.radians(degrees)), 0],
                      [math.sin(math.radians(degrees)), math.cos(math.radians(degrees)), 0],
                      [0, 0, 1]])
        self.currentTransformation = r.dot(self.currentTransformation)
    '''
     *
     * scale - Add a scale to the current transformation by premultiplying the appropriate
     *          scaling matrix to the current transformtion matrix.
     *
     * @param x - Amount of scaling in x.
     * @param y - Amount of scaling in y.
     *
    '''
    def scale(self,x,y):
        '''
        function that adds a scale to the current transformation by pre-multiplying the
        scaling matrix to the current transformation matrix
        :param x: amount of scaling in x
        :param y: amount of scaling in y
        '''
        s = np.array([[x, 0, 0],
                      [0, y, 0],
                      [0, 0, 1]])
        self.currentTransformation = s.dot(self.currentTransformation)
    '''
     *
     * translate - Add a translation to the current transformation by premultiplying the appropriate
     *          translation matrix to the current transformtion matrix.
     *
     * @param x - Amount of translation in x.
     * @param y - Amount of translation in y.
     *
    '''
    def translate(self,x, y):
        '''
        function that adds a translation to the current transformation by pre-multiplying the
        translation matrix to the current transformation matrix
        :param x: amount of translation in x
        :param y: amount of translation in y
        '''
        t = np.array([[1, 0, x],
                      [0, 1, y],
                      [0, 0, 1]])
        self.currentTransformation = t.dot(self.currentTransformation)
    '''
     *
     * setClipWindow - defines the clip window
     *
     * @param bottom - y coord of bottom edge of clip window (in world coords)
     * @param top - y coord of top edge of clip window (in world coords)
     * @param left - x coord of left edge of clip window (in world coords)
     * @param right - x coord of right edge of clip window (in world coords)
     *
    '''
    def setClipWindow(self, bottom, top, left, right):
        '''
        function that defines the clip window
        :param bottom: y coord of bottom edge of clip window
        :param top: y coord of top edge of clip window
        :param left: x coord of left edge of clip window
        :param right: x coord of right edge of clip window
        '''
        self.bottom = bottom
        self.top = top
        self.right = right
        self.left = left

    '''
     *
     * setViewport - defines the viewport
     *
     * @param xmin - x coord of lower left of view window (in screen coords)
     * @param ymin - y coord of lower left of view window (in screen coords)
     * @param width - width of view window (in world coords)
     * @param height - width of view window (in world coords)
     *
    '''
    def setViewport(self,x,y,width,height):
        '''
        function that defines the viewport
        :param x: x coord of lower left of view window
        :param y: y coord of lower left of view window
        :param width: width of view window
        :param height: width of view window
        '''
        xvmin = x
        xvmax = x + width
        yvmin = y
        yvmax = y + height
        sx = (xvmax - xvmin) / ((self.right - self.left) * 1.0)
        sy = (yvmax - yvmin) / ((self.top - self.bottom) * 1.0)
        tx = ((self.right * xvmin) - (self.left * xvmax)) / ((self.right - self.left) * 1.0)
        ty = ((self.top * yvmin) - (self.bottom * yvmax)) / ((self.top - self.bottom) * 1.0)
        self.viewTransform[0, 0] = sx
        self.viewTransform[0, 1] = 0
        self.viewTransform[0, 2] = tx
        self.viewTransform[1, 0] = 0
        self.viewTransform[1, 1] = sy
        self.viewTransform[1, 2] = ty
        self.viewTransform[2, 0] = 0
        self.viewTransform[2, 1] = 0
        self.viewTransform[2, 2] = 1