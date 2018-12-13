# Clipper.py
#
# Created on June 12, 2016
#
# @author: Srinivas
#
# Contributor:  Hiteshi Shah (hss7374)
# 
# Object for performing clipping

class clipper(object):
    #   clipPolygon
    #
    #   Clip the polygon with vertex count in and vertices inx/iny
    #   against the rectangular clipping region specified by lower-left corner
    #   (llx,lly) and upper-right corner (urx,ury). The resulting vertices are
    #   placed in outx/outy.
    #
    #   The routine should return the with the vertex count of polygon
    #   resultinhg from the clipping.
    #
    #   @param in the number of vertices in the polygon to be clipped
    #   @param inx - x coords of vertices of polygon to be clipped.
    #   @param iny - y coords of vertices of polygon to be clipped.
    #   @param outx - x coords of vertices of polygon resulting after clipping.
    #   @param outy - y coords of vertices of polygon resulting after clipping.
    #   @param llx - x coord of lower left of clipping rectangle.
    #   @param lly - y coord of lower left of clipping rectangle.
    #   @param urx - x coord of upper right of clipping rectangle.
    #   @param ury - y coord of upper right of clipping rectangle.
    #
    #   @return number of vertices in the polygon resulting after clipping

    def clipPolygon(self,in1,inx,iny,outx,outy,llx,lly,urx,ury):
        '''
        function to clip a polygon, given the co-ordinates of the polygon as well as the clip window
        :param in1: number of vertices in the polygon
        :param inx: list of x-coordinates of the polygon vertices before clipping
        :param iny: list of y-coordinates of the polygon vertices before clipping
        :param outx: list of x-coordinates of the polygon vertices after clipping
        :param outy: list of y-coordinates of the polygon vertices after clipping
        :param llx: lower-left x-coordinate of the clip window
        :param lly: lower-left y-coordinate of the clip window
        :param urx: upper-right x-coordinate of the clip window
        :param ury: upper-right y-coordinate of the clip window
        :return: number of vertices in the polygon resulting after clipping
        '''

        # clipping the polygon against the right side of the clip window
        n1, inx, iny = self.right_clip(in1, inx, iny, urx)

        # updating the number of vertices after clipping
        in1 = len(inx)

        # clipping the polygon against the top side of the clip window
        n2, inx, iny = self.top_clip(in1, inx, iny, ury)

        # updating the number of vertices after clipping
        in1 = len(inx)

        # clipping the polygon against the bottom side of the clip window
        n3, inx, iny = self.bottom_clip(in1, inx, iny, lly)

        # updating the number of vertices after clipping
        in1 = len(inx)

        # clipping the polygon against the left side of the clip window
        n4, inx, iny = self.left_clip(in1, inx, iny, llx)

        outx[:] = inx
        outy[:] = iny

        return n4

    def right_clip(self, in1, inx, iny, urx):
        '''
        function to clip the polygon against the right plane of the clip window
        :param in1: number of vertices in the polygon
        :param inx: list of x-coordinates of the polygon vertices before clipping
        :param iny: list of y-coordinates of the polygon vertices before clipping
        :param urx: right plane of the clipping window
        :return: n: number of vertices in the polygon resulting after clipping against the right plane
                 outx: list of x-coordinates of the polygon vertices after clipping against the right plane
                 outy: list of y-coordinates of the polygon vertices after clipping against the right plane
        '''

        outx = []           # initializing the list of x-coordinates of the polygon vertices after clipping
        outy = []           # initializing the list of y-coordinates of the polygon vertices after clipping

        n = 0               # initializing the number of vertices in the polygon resulting after clipping

        Sx = inx[in1 - 1]   # x-coordinate of the first point S in the current polygon edge
        Sy = iny[in1 - 1]   # y-coordinate of the first point S in the current polygon edge

        for j in range(0, in1):
            Px = inx[j]     # x-coordinate of the second point P in the current polygon edge
            Py = iny[j]     # y-coordinate of the second point P in the current polygon edge

            # if the point P is inside the clip plane
            if Px < urx:
                # if the point S is outside the clip plane
                if Sx >= urx:
                    # calculating the intersection point and appending to the lists
                    slope = (Py - Sy) / ((Px - Sx) * 1.0)
                    outx.append(urx)
                    outy.append(slope * (urx - Sx) + Sy)
                    n += 1
                outx.append(Px)
                outy.append(Py)
            # if the point P is outside the clip plane
            else:
                # if the point S is inside the clip place
                if Sx < urx:
                    # calculating the intersection point and appending to the lists
                    slope = (Py - Sy) / ((Px - Sx) * 1.0)
                    outx.append(urx)
                    outy.append(slope * (urx - Sx) + Sy)
                    n += 1
            Sx = Px
            Sy = Py

        if len(outx) == 0:
            outx = inx

        if len(outy) == 0:
            outy = iny

        return n, outx, outy

    def top_clip(self, in1, inx, iny, ury):
        '''
        function to clip the polygon against the top plane of the clip window
        :param in1: number of vertices in the polygon
        :param inx: list of x-coordinates of the polygon vertices before clipping
        :param iny: list of y-coordinates of the polygon vertices before clipping
        :param ury: top plane of the clipping window
        :return: n: number of vertices in the polygon resulting after clipping against the top plane
                 outx: list of x-coordinates of the polygon vertices after clipping against the top plane
                 outy: list of y-coordinates of the polygon vertices after clipping against the top plane
        '''

        outx = []  # initializing the list of x-coordinates of the polygon vertices after clipping
        outy = []  # initializing the list of y-coordinates of the polygon vertices after clipping

        n = 0  # initializing the number of vertices in the polygon resulting after clipping

        Sx = inx[in1 - 1]  # x-coordinate of the first point S in the current polygon edge
        Sy = iny[in1 - 1]  # y-coordinate of the first point S in the current polygon edge

        for j in range(0, in1):
            Px = inx[j]  # x-coordinate of the second point P in the current polygon edge
            Py = iny[j]  # y-coordinate of the second point P in the current polygon edge

            # if the point P is inside the clip plane
            if Py < ury:
                # if the point S is outside the cip plane
                if Sy >= ury:
                    # calculating the intersection point and appending to the lists
                    if (Px - Sx) != 0:
                        slope = (Py - Sy) / ((Px - Sx) * 1.0)
                        outx.append(Sx + (ury - Sy) / slope)
                    else:
                        outx.append(Sx)
                    outy.append(ury)
                    n += 1
                outx.append(Px)
                outy.append(Py)
            # if the point P is outside the clip plane
            else:
                # if the point S is inside the clip plane
                if Sy < ury:
                    # calculating the intersection point and appending to the lists
                    if (Px - Sx) != 0:
                        slope = (Py - Sy) / ((Px - Sx) * 1.0)
                        outx.append(Sx + (ury - Sy) / slope)
                    else:
                        outx.append(Sx)
                    outy.append(ury)
                    n += 1
            Sx = Px
            Sy = Py

        if len(outx) == 0:
            outx = inx

        if len(outy) == 0:
            outy = iny

        return n, outx, outy

    def bottom_clip(self, in1, inx, iny, lly):
        '''
        function to clip the polygon against the bottom plane of the clip window
        :param in1: number of vertices in the polygon
        :param inx: list of x-coordinates of the polygon vertices before clipping
        :param iny: list of y-coordinates of the polygon vertices before clipping
        :param lly: bottom plane of the clipping window
        :return: n: number of vertices in the polygon resulting after clipping against the bottom plane
                 outx: list of x-coordinates of the polygon vertices after clipping against the bottom plane
                 outy: list of y-coordinates of the polygon vertices after clipping against the bottom plane
        '''

        outx = []  # initializing the list of x-coordinates of the polygon vertices after clipping
        outy = []  # initializing the list of y-coordinates of the polygon vertices after clipping

        n = 0  # initializing the number of vertices in the polygon resulting after clipping

        Sx = inx[in1 - 1]  # x-coordinate of the first point S in the current polygon edge
        Sy = iny[in1 - 1]  # y-coordinate of the first point S in the current polygon edge

        for j in range(0, in1):
            Px = inx[j]  # x-coordinate of the second point P in the current polygon edge
            Py = iny[j]  # y-coordinate of the second point P in the current polygon edge

            # if the point P is inside the clip plane
            if Py >= lly:
                # if the pont S is outside the clip plane
                if Sy < lly:
                    # calculating the intersection point and appending to the lists
                    if (Px - Sx) != 0:
                        slope = (Py - Sy) / ((Px - Sx) * 1.0)
                        outx.append(Sx + (lly - Sy) / slope)
                    else:
                        outx.append(Sx)
                    outy.append(lly)
                    n += 1
                outx.append(Px)
                outy.append(Py)
            # if the point P is outside the clip plane
            else:
                # if the point S is inside the clip plane
                if Sy >= lly:
                    # calculating the intersection point and appending to the lists
                    if (Px - Sx) != 0:
                        slope = (Py - Sy) / ((Px - Sx) * 1.0)
                        outx.append(Sx + (lly - Sy) / slope)
                    else:
                        outx.append(Sx)
                    outy.append(lly)
                    n += 1
            Sx = Px
            Sy = Py

        if len(outx) == 0:
            outx = inx

        if len(outy) == 0:
            outy = iny

        return n, outx, outy

    def left_clip(self, in1, inx, iny, llx):
        '''
        function to clip the polygon against the left plane of the clip window
        :param in1: number of vertices in the polygon
        :param inx: list of x-coordinates of the polygon vertices before clipping
        :param iny: list of y-coordinates of the polygon vertices before clipping
        :param llx: left plane of the clipping window
        :return: n: number of vertices in the polygon resulting after clipping against the left plane
                 outx: list of x-coordinates of the polygon vertices after clipping against the left plane
                 outy: list of y-coordinates of the polygon vertices after clipping against the left plane
        '''

        outx = []  # initializing the list of x-coordinates of the polygon vertices after clipping
        outy = []  # initializing the list of y-coordinates of the polygon vertices after clipping

        n = 0  # initializing the number of vertices in the polygon resulting after clipping

        Sx = inx[in1 - 1]  # x-coordinate of the first point S in the current polygon edge
        Sy = iny[in1 - 1]  # y-coordinate of the first point S in the current polygon edge

        for j in range(0, in1):
            Px = inx[j]  # x-coordinate of the second point P in the current polygon edge
            Py = iny[j]  # y-coordinate of the second point P in the current polygon edge

            # if the point P is inside the clip plane
            if Px >= llx:
                # if the point S is outside the clip plane
                if Sx < llx:
                    # calculating the intersection point and appending to the lists
                    slope = (Py - Sy) / ((Px - Sx) * 1.0)
                    outx.append(llx)
                    outy.append(slope * (llx - Sx) + Sy)
                    n += 1
                outx.append(Px)
                outy.append(Py)
            # if the point P is outside the clip plane
            else:
                # if the point S is inside the clip plane
                if Sx >= llx:
                    # calculating the intersection point and appending to the lists
                    slope = (Py - Sy) / ((Px - Sx) * 1.0)
                    outx.append(llx)
                    outy.append(slope * (llx - Sx) + Sy)
                    n += 1
            Sx = Px
            Sy = Py

        if len(outx) == 0:
            outx = inx

        if len(outy) == 0:
            outy = iny

        return n, outx, outy