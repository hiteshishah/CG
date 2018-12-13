'''

@author: Hiteshi Shah
'''


class Rasterization(object):

    scan_line = 0

    def __init__(self,n):
        self.scan_line = n

    '''
    Draw a filled polygon in the simpleCanvas sc.

    The polygon has n distinct vertices. The
    coordinates of the vertices making up the polygon are stored in the
    x and y lists.  The ith vertex will have coordinate  (x[i], y[i])

    You are to add the implementation here using only calls
    to sc.setPixel()
    '''

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

    def drawPolygon(self, n,x,y,sc):
        '''
        function that draw a polygon given the number of vertices and the lists of x- and y-coordinates
        :param n: the number of vertices of the polygon to be drawn
        :param x: list of x-coordinates
        :param y: list of y-coordinates
        :param sc: the SimpleCanvas object
        '''

        edge_table = self.createEdgeTable(n, x, y)

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
            active_list = sorted(active_list, key=lambda a:a[2])

            # filling the polygon for the current scan line
            for edge in range(1, len(active_list), 2):
                for x in range(active_list[edge - 1][2], active_list[edge][2]):
                    sc.setPixel(x, scan_line)

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