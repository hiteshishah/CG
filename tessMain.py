'''
Created on Nov 5, 2014

@author: Srinivas
'''
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from shaderSetup import shaderSetup
from cgShape import cgShape
from bufferSet import *
from numpy import array, arange
import math
import timeit


class tessMain(object):

    #program ID returned from Shader Program
    programID = None
    
    # The shapes we can draw
    CUBE = "CUBE"
    CYLINDER = "CYLINDER"
    CONE = "CONE"
    SPHERE = "SPHERE"
    
    currentShape = CUBE
    
    # Dimensions of the drawing window
    w_witdh = 512
    w_height = 512
    
    # Subdivsions for tesselation
    division1 = 1
    division2 = 1
    
    # Are we animating?
    #animating = false;
    
    # do we need to do a display() call?
    updateDisplay = True
    
    # our canvas
    myShape = cgShape(None)
    
    # Buffer Info
    shapeBuffers = bufferSet (None)
    
    # GLSL shader program handle
    program = 0
    
    # shader arguments
    theta = 0
    vPosition = 0
    
    # rotation control
    anglesReset = [30.0, 30.0, 0.0]
    angles = [30.0, 30.0, 0.0]
    angleInc = 5.0
    
    # vertex array object
    vaoID = GLuint(0)
    
    def createNewShape(self):
        
        # clear the old shape
        self.myShape.clear()
        
        # create the new shape
        if(self.currentShape.lower() == self.CUBE.lower()):
            self.myShape.makeCube(self.division1)
        elif(self.currentShape.lower() == self.CYLINDER.lower()):
            self.myShape.makeCylinder(0.5, self.division1, self.division2)
        elif(self.currentShape.lower() == self.CONE.lower()):
            self.myShape.makeCone(0.5, self.division1, self.division2)
        elif(self.currentShape.lower() == self.SPHERE.lower()):
            self.myShape.makeSphere(0.5, self.division1, self.division2)
        else:
            print ("Other shapes are not programmed check with developer to add new shapes")

        self.shapeBuffers.createBuffers (self.myShape)

        self.updateDisplay = True

    def init (self):
    
        myShaders = shaderSetup(None)
        self.programID = myShaders.readAndCompile("shader.vert", "shader.frag")
    
        #Check the program ID
        if self.programID <= 0:
            print ("Error setting up program ID")
            raise Exception("Error setting up program ID", "fatal")
            sys.exit(1)
        
        #set up a vertex array object...required for Python
        glGenVertexArrays(1, self.vaoID)
        glBindVertexArray (self.vaoID)
    
        #Generate and Bind vertex buffer and load vertex data
        glUseProgram(self.programID)
        self.vPosition = glGetAttribLocation (self.programID, "vPosition")
        self.theta = glGetUniformLocation (self.programID, "theta")
        
        #Other GL initialization
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        
        glCullFace(GL_BACK)
        glFrontFace(GL_CCW)
        glClearColor(0.0,0.0,0.0,1.0)
        glDepthFunc(GL_LEQUAL)
        glClearDepth(1.0)

        self.createNewShape()
            
            
    #  bind the correct vertex and element buffere
    def selectBuffers (self, program, B) :

        #bind the buffers
        glBindVertexArray (self.vaoID)
        glBindBuffer( GL_ARRAY_BUFFER, B.vbuffer );
        glBindBuffer( GL_ELEMENT_ARRAY_BUFFER, B.ebuffer );
    
        # set up the vertex attribute variables
        glEnableVertexAttribArray( self.vPosition );
        glVertexAttribPointer( self.vPosition, 4, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0) );
        
        # send down our rotation angles
        glUniform3fv( self.theta, 1, self.angles );

    # display function
    def display (self) :
        # clear the frame buffer
        glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );
    
        # bind our buffers
        self.selectBuffers( self.program, self.shapeBuffers );
    
        # draw our shape
        if (self.shapeBuffers.numElements > 0 ):
            glDrawArrays(GL_TRIANGLES, 0, self.shapeBuffers.numElements)
        
        #Swap the buffers
        glutSwapBuffers()

# can cause gimble lock
    def animate(self):
        for incr1 in range(0,150):
            self.angles[0] = self.angles[0] + (self.angleInc /3)
            self.glDraw()
        for incr2 in range(0,150):
            self.angles[1] = self.angles[1] + (self.angleInc /3)
            self.glDraw()
        for incr3 in range(0,150):
            self.angles[2] = self.angles[2] + (self.angleInc /3)
            self.glDraw()
        
    '''
     * Notifies the listener to perform the release of all OpenGL 
     * resources per GLContext, such as memory buffers and GLSL 
     * programs.
    '''    
    def dispose(self):
        #Clean up code
        nfe = error.NullFunctionError
        self.timer.stop()
        self.timer.timeout.disconnect(self.idleGL)

        glDeleteProgram(self.programID)
        try:
            glDeleteBuffers(1, GLuint(self.vbuffer))
            glDeleteBuffers(1, GLuint(self.ebuffer))
        except (AttributeError, nfe):
            pass

    # keyboard function
    def keyPressed(self,*args):
    
        #Get the key that was pressed
        key = str(args[0].decode())
    
        # auto animation
        if(key == 'a' or key == 'A'):
        #self.animating = true
            pass
        
        # incremental rotation
        elif(key == 'x'):
            self.angles[0] -= self.angleInc
        elif(key == 'y'):
            self.angles[1] -= self.angleInc
        elif(key == 'z'):
            self.angles[2] -= self.angleInc
        elif(key == 'X'):
            self.angles[0] += self.angleInc
        elif(key == 'Y'):
            self.angles[1] += self.angleInc
        elif(key == 'X'):
            self.angles[2] += self.angleInc

        # shape selection
        elif (key == '1' or key == 'c') :
            self.currentShape = self.CUBE
            self.createNewShape()
        elif (key == '2' or key == 'C') :
            self.currentShape = self.CYLINDER
            self.createNewShape()
        elif (key == '3' or key == 'n') :
            self.currentShape = self.CONE
            self.createNewShape()
        elif (key == '4' or key == 's') :
            self.currentShape = self.SPHERE
            self.createNewShape()

        # tessellation control
        elif (key == '+') :
            self.division1 = self.division1 + 1
            self.createNewShape()
        elif (key == '=') :
            self.division2 = self.division2 + 1
            self.createNewShape()
        elif (key == '-') :
            if (self.division1 > 1) :
                self.division1 = self.division1 - 1
                self.createNewShape()
        elif (key == '_') :
            if (self.division2 > 1) :
                self.division2 = self.division2 - 1;
                if (self.currentShape != self.CUBE) :
                    self.createNewShape()

        # reset
        elif (key == 'r' or key=='R') :
            self.angles[0] = self.anglesReset[0]
            self.angles[1] = self.anglesReset[1]
            self.angles[2] = self.anglesReset[2]

        # termination
        elif(key == 'q' or key == 'Q'):
            sys.exit()
        elif(args[0] == '\033'): #Escape character
            sys.exit()

        updateDisplay = True

    def dispose(self):
        #Clean up code
        glDeleteProgram(self.shaderProgID)
        glDeleteBuffers(1, GLuint(self.vbuffer1))
        glDeleteBuffers(1, GLuint(self.vbuffer2))
        glDeleteBuffers(1, GLuint(self.ebuffer))
    
    
    def reshape(self, x,y,widht,height):
        pass
    
    def keyTyped(self):
        pass
    
    def keyRelease(self):
        pass

    def main(self):
    
        glutInit()
        glutInitDisplayMode(GLUT_RGBA|GLUT_ALPHA|GLUT_DOUBLE|GLUT_DEPTH|GLUT_3_2_CORE_PROFILE)
        glutInitWindowSize(512,512)
        glutCreateWindow(b"Tesselation Demo")
    
        self.init()
        
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutKeyboardFunc(self.keyPressed)
        
        glutMainLoop()
        
        self.dispose()

if __name__ == "__main__":
    tessMain().main()
