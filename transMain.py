import sys

from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import array, arange
from teapot import teapot
from shaderSetup import shaderSetup
from viewParams import viewParams
from simpleShape import *
from bufferSet import *

class transMain (object) :
    
    # do we need to do a display() call?
    updateDisplay = True
    
    # our viewparams
    view = viewParams ()
    
    # dimensions of the drawing window
    w_width  = 512
    w_height = 512

    # buffer information
    shapeBuffers = bufferSet(None)

    # mouse click tracker
    counter = 0

    # flags controlling drawing options
    cameraAdjust = False
    transformsOn = False
    viewMode = 1

    # program IDs...for program and parameters
    programID = GLuint (0)

    # vertex array object
    vaoID = GLuint(0)
    
    #
    # initialization
    #
    def init (self):

        # Load shaders and use the resulting shader program
        myShaders = shaderSetup(None)
        self.programID = myShaders.readAndCompile("shader.vert", "shader.frag")
        
        #Check the program ID
        if self.programID <= 0:
            print ("Error setting up program ID")
            raise Exception("Error setting up program ID", "fatal")
            sys.exit(1)

        # create the geometry for your shapes.
        myShape = teapot()
        myShape.clear()
        myShape.makeTeapot()

        #set up a vertex array object...required for Python
        self.vaoID = self.createVAO(myShape)
    
        # Other OpenGL initialization
        glEnable( GL_DEPTH_TEST )
        glEnable( GL_CULL_FACE )
        glCullFace( GL_BACK )
        glClearColor( 1.0, 1.0, 1.0, 1.0 )
        glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
        glClearDepth( 1.0 )

            
    '''
    * Creates VAO for given set of objects.  Returns the VAO ID
    '''
    def createVAO (self, shape) :
        
        # Get yourself an ID
        vaoID = GLuint(0)
        glGenVertexArrays(1, vaoID)
        
        # You'll need the correct program to get the location of the vertex
        # attributes
        glUseProgram(self.programID)
        vPosition = glGetAttribLocation(self.programID,"vPosition")

        # Bind the vertex array object
        glBindVertexArray (vaoID)
        
        # Make and fill your buffer
        # create the buffers
        self.shapeBuffers.createBuffers (shape)
        
        # set buffers to correct vertext attribute
        glEnableVertexAttribArray(vPosition)
        glVertexAttribPointer(vPosition,4,GL_FLOAT,GL_FALSE,0,ctypes.c_void_p(0))
        
        # return your ID
        return vaoID

    #
    # keyboard function
    #
    def keyPressed(self,*args):
    
        #Get the key that was pressed
        key = str(args[0].decode())
    
        # view mode
        if(key == '1'):
            self.viewMode = 1
            self.updateDisplay = True
        elif (key == '2') :
            self.viewMode = 2;
            self.updateDisplay = True
                
        # cycle through transforms (same as mouse clicks in C++ version
        elif (key == ' ') :

            self.counter = self.counter + 1
            c4 = self.counter % 4
            if (c4 == 0) :
                # default camera, no transforms
                self.cameraAdjust = False
                self.transformsOn = False

            elif (c4 == 1):
                # default camera, turn on transformations
                self.cameraAdjust = False
                self.transformsOn = True

            elif (c4 == 2) :
                # modified camera, no transforms
                self.cameraAdjust = True
                self.transformsOn = False
                    
            else :
                # modified camera, transformations
                self.cameraAdjust = True
                self.transformsOn = True
                    
            self.updateDisplay = True
                
        # quit
        elif(key == 'q' or key == 'Q'):
            sys.exit()
        elif(args[0] == '\033'): #Escape character
            sys.exit()

    #
    # display function
    #
    def display( self ) :
        
        # clear the frame buffer
        glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    
        # bind our buffers
        #self.selectBuffers( self.programID, self.shapeBuffers );
    
        # set up viewing and projection parameters
        if( self.viewMode == 1 ) :
            self.view.setUpFrustrum( self.programID )
        elif( self. viewMode == 2 ) :
            self.view.setUpOrtho( self.programID )
        else :
            print ("unknown viewing mode -- resetting")
            self.viewMode = 1
            self.view.setUpFrustrum( self.programID )

        # set up the camera
        #
        # changing the camera sets eyepoint to (0,1.3,-0.5), lookat
        # to (0,-0.4,-1.0), and up to (0,1,0)
        if( self.cameraAdjust ) :
            self.view.setUpCamera( self.programID, 0.0, 1.3, -0.5, 0.0, -0.4, -1.0, 0.0, 1.0, 0.0 )
        else :
            self.view.clearCamera( self.programID )

        # set up transformations
        #
        # transformations are applied in this order (if you are having
        # trouble recreating the solution image, check your order of
        # matrix multiplication):
        #
        #   scale Y by 2
        #   rotate around Z by 335 degrees
        #   rotate around Y by 10 degrees
        #   translate in X by -0.2
        #   translate in Y by 0.2
        if( self.transformsOn ) :
            self.view.setUpTransform( self.programID, 1.0, 2.0, 1.0, 0.0, 10.0, 335.0, -0.2, 0.2, 0.0 )
        else:
            self.view.clearTransform( self.programID )
    
        # draw your shape
        glBindVertexArray (self.vaoID)
        glDrawArrays(GL_TRIANGLES, 0, self.shapeBuffers.numElements)

        #Swap the buffers
        glutSwapBuffers()

    def main(self):
    
        glutInit()
        glutInitDisplayMode(GLUT_RGBA|GLUT_ALPHA|GLUT_DOUBLE|GLUT_DEPTH|GLUT_3_2_CORE_PROFILE)
        glutInitWindowSize(512,512)
        glutCreateWindow("Transformation Demo")
    
        self.init()
    
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutKeyboardFunc(self.keyPressed)
        
        glutMainLoop()
        
        self.dispose()


if __name__ == '__main__':
    transMain().main()
