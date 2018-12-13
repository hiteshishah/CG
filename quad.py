'''
//  quad.py
//
//  Routines for tessellating a standard quad.
//  The quad is parallel to the XY plane with the front face
// pointing down the +Z axis
//
//  Students should not be modifying this file.
//
//  @author Srini
'''

from simpleShape import simpleShape

class quad (simpleShape):

    quadVertices = [
    # top row
    -0.50,  0.50,  0.50, -0.25,  0.50,  0.50,  0.00,  0.50,  0.50,
        0.25,  0.50,  0.50,  0.50,  0.50,  0.50,
    # second row
    -0.50,  0.25,  0.50, -0.25,  0.25,  0.50,  0.00,  0.25,  0.50,
        0.25,  0.25,  0.50,  0.50,  0.25,  0.50,
    # third (middle) row
    -0.50,  0.00,  0.50, -0.25,  0.00,  0.50,  0.00,  0.00,  0.50,
        0.25,  0.00,  0.50,  0.50,  0.00,  0.50,
    # fourth row
    -0.50, -0.25,  0.50, -0.25, -0.25,  0.50,  0.00, -0.25,  0.50,
        0.25, -0.25,  0.50,  0.50, -0.25,  0.50,
    # fifth (last) row
    -0.50, -0.50,  0.50, -0.25, -0.50,  0.50,  0.00, -0.50,  0.50,
        0.25, -0.50,  0.50,  0.50, -0.50,  0.50 ]
        
    quadVerticesLength = len(quadVertices)

    #
    # Each pair of values specifies a vertex's texture coordinates
    #
    quadUV = [
    #top row
    0.00, 1.00, 0.25, 1.00, 0.50, 1.00, 0.75, 1.00, 1.00, 1.00,
    # second row
    0.00, 0.75, 0.25, 0.75, 0.50, 0.75, 0.75, 0.75, 1.00, 0.75,
    # third (middle) row
    0.00, 0.50, 0.25, 0.50, 0.50, 0.50, 0.75, 0.50, 1.00, 0.50,
    # fourth row
    0.00, 0.25, 0.25, 0.25, 0.50, 0.25, 0.75, 0.25, 1.00, 0.25,
    # fifth (last) row
    0.00, 0.00, 0.25, 0.00, 0.50, 0.00, 0.75, 0.00, 1.00, 0.00 ]


    #
    # Because the quad faces +Z, all the normals are (0,0,1)
    #
    quadNormals = [ 0.0, 0.0, 1.0 ];

    quadNormalsLength = len (quadNormals)

    #
    # Each group of three entries specifies a triangle for the quad
    #
    quadElements = [
    # top row
    0,  5,  1,  5,  6,  1,  1,  6,  2,  6,  7,  2,
    2,  7,  3,  7,  8,  3,  3,  8,  4,  8,  9,  4,
    # second row
    5, 10,  6, 10, 11,  6,  6, 11,  7, 11, 12,  7,
    7, 12,  8, 12, 13,  8,  8, 13,  9, 13, 14,  9,
    #  third row
    10, 15, 11, 15, 16, 11, 11, 16, 12, 16, 17, 12,
    12, 17, 13, 17, 18, 13, 13, 18, 14, 18, 19, 14,
    # fourth row
    15, 20, 16, 20, 21, 16, 16, 21, 17, 21, 22, 17,
    17, 22, 18, 22, 23, 18, 18, 23, 19, 23, 24, 19 ]

    quadElementsLength = len (quadElements)

    def makeQuad (self) :

        for i in range(0, self.quadElementsLength - 2 ,3):
        
            # Calculate the base indices of the three vertices
            point1 = 3 * self.quadElements[i];     # slots 0, 1, 2
            point2 = 3 * self.quadElements[i + 1]; # slots 3, 4, 5
            point3 = 3 * self.quadElements[i + 2]; # slots 6, 7, 8
                
            # Calculate the base indices of the three texture coordinates
            normal1 = 2 * self.quadElements[i];     # slots 0, 1, 2
            normal2 = 2 * self.quadElements[i + 1]; # slots 3, 4, 5
            normal3 = 2 * self.quadElements[i + 2]; # slots 6, 7, 8
                
            # Add triangle and texture coordinates
            self.addTriangleWithUV( self.quadVertices[point1 + 0],self.quadVertices[point1 + 1],self.quadVertices[point1 + 2], self.quadVertices[point2 + 0], self.quadVertices[point2 + 1], self.quadVertices[point2 + 2], self.quadVertices[point3 + 0],self.quadVertices[point3 + 1],self.quadVertices[point3 + 2], self.quadUV[normal1 + 0],self.quadUV[normal1 + 1],self.quadUV[normal2 + 0],self.quadUV[normal2 + 1],self.quadUV[normal3 + 0], self.quadUV[normal3 + 1])
                    

    def __init__(self):
        pass

 
