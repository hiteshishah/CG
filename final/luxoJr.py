'''
//  luxoJr.py
//
//  File for executing the 3D pipeline
//
//  Name: Hiteshi Shah (hss7374)
'''


from OpenGL.GLUT import *
from ball import ball
from base import base
from stand import stand
from quad import quad
from tilt import tilt
from lamp import lamp
from shaderSetup import shaderSetup
from viewParams import viewParams
from textures import *
from lighting import *
from baselight import *
from standlight import *
from tiltlight import *
from lamplight import *
from bufferSet import *

class luxoJr (object) :
    
    # the viewparams
    view = viewParams ()
    
    # lighting and textures
    tex = textures ()
    light = lighting()
    baselight = baselight()
    standlight = standlight()
    tiltlight = tiltlight()
    lamplight = lamplight()

    # dimensions of the drawing window
    w_width  = 600
    w_height = 600

    # buffer information
    quadBuffers = bufferSet(None)
    ballBuffers = bufferSet(None)
    baseBuffers = bufferSet(None)
    standBuffers = bufferSet(None)
    tiltBuffers = bufferSet(None)
    lampBuffers = bufferSet(None)

    # program IDs...for program and parameters
    pshader = GLuint (0)
    tshader = GLuint (0)
    bshader = GLuint(0)
    sshader = GLuint(0)
    lshader = GLuint(0)
    cshader = GLuint(0)

    # vertex array object
    qVao = GLuint(0)
    tVao = GLuint(0)
    bVao = GLuint(0)
    sVao = GLuint(0)
    lVao = GLuint(0)
    cVao = GLuint(0)

    # animation flags
    animating1 = True
    animating2 = False

    # variables for animation
    transBall = 3.0
    rotBall = 0.0

    def init (self):
        '''
        function for initialization
        '''
        
        # Load textures
        self.tex.loadTexture()

        # Load shaders and verify each
        myShaders = shaderSetup(None)
        self.tshader = myShaders.readAndCompile("texture.vert", "texture.frag")
        if self.tshader <= 0:
            print ("Error setting up Texture shaders")
            raise Exception("Error setting up Texture Shaders", "fatal")
            sys.exit(1)
        
        self.pshader = myShaders.readAndCompile("ball.vert", "ball.frag")
        if self.pshader <= 0:
            print ("Error setting up Phong shaders")
            raise Exception("Error setting up Phong Shaders", "fatal")
            sys.exit(1)

        self.bshader = myShaders.readAndCompile("base.vert", "base.frag")
        if self.bshader <= 0:
            print ("Error setting up Base shaders")
            raise Exception("Error setting up Base Shaders", "fatal")
            sys.exit(1)

        self.sshader = myShaders.readAndCompile("stand.vert", "stand.frag")
        if self.sshader <= 0:
            print ("Error setting up Stand shaders")
            raise Exception("Error setting up Stand Shaders", "fatal")
            sys.exit(1)

        self.lshader = myShaders.readAndCompile("tilt.vert", "tilt.frag")
        if self.lshader <= 0:
            print ("Error setting up Tilt shaders")
            raise Exception("Error setting up Tilt Shaders", "fatal")
            sys.exit(1)

        self.cshader = myShaders.readAndCompile("lamp.vert", "lamp.frag")
        if self.cshader <= 0:
            print ("Error setting up Lamp shaders")
            raise Exception("Error setting up Lamp Shaders", "fatal")
            sys.exit(1)
                
        # Other OpenGL initialization
        glEnable( GL_DEPTH_TEST )
        glClearColor( 0.0, 0.0, 0.0, 0.0 )
        glPolygonMode( GL_FRONT_AND_BACK, GL_FILL )
        glClearDepth( 1.0 )

        # create ball
        myShape = ball()
        myShape.clear()
        myShape.makeSphere(0.3, 30, 1)
        self.tVao = self.createVAO(myShape, self.pshader, self.ballBuffers )
            
        # create quad
        myShape = quad ()
        myShape.clear()
        myShape.makeQuad()
        self.qVao = self.createVAO(myShape, self.tshader, self.quadBuffers )

        # create base
        myShape = base()
        myShape.clear()
        myShape.makeCylinder(80)
        self.bVao = self.createVAO(myShape, self.bshader, self.baseBuffers)

        # create stand
        myShape = stand()
        myShape.clear()
        myShape.makeStand(80)
        self.sVao = self.createVAO(myShape, self.sshader, self.standBuffers)

        # create tilt
        myShape = tilt()
        myShape.clear()
        myShape.makeTilt(80)
        self.lVao = self.createVAO(myShape, self.lshader, self.tiltBuffers)

        # create lamp
        myShape = lamp()
        myShape.clear()
        myShape.makeCone(0.3, 50, 50)
        self.cVao = self.createVAO(myShape, self.cshader, self.lampBuffers)


    def createVAO (self, shape, program, B) :
        '''
        function to create VAO for given set of objects
        :param shape: shape to create
        :param program: program ID
        :param B: buffer information
        :return VAO ID
        '''
        
        # Get an ID
        vaoID = GLuint(0)
        glGenVertexArrays(1, vaoID)
        
        # Using the correct program to get the location of the vertex attributes
        glUseProgram(program)
        
        # Bind the vertex array object
        glBindVertexArray (vaoID)
        
        # Make and fill buffer
        # create the buffers
        B.createBuffers (shape)
        
        # set buffers to correct vertext attribute
        vPosition = glGetAttribLocation(program,"vPosition")
        glEnableVertexAttribArray(vPosition)
        glBindBuffer (GL_ARRAY_BUFFER, B.vbuffer)
        glVertexAttribPointer(vPosition,4,GL_FLOAT,GL_FALSE,0,ctypes.c_void_p(0))
        
        # color data
        if( B.cSize > 0) :
            vColor = glGetAttribLocation( program, "vColor" )
            glEnableVertexAttribArray( vColor )
            glBindBuffer (GL_ARRAY_BUFFER, B.cbuffer)
            glVertexAttribPointer( vColor, 4, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p (0))

        # normal data
        if( B.nSize > 0 ) :
            vNormal = glGetAttribLocation( program, "vNormal" )
            glEnableVertexAttribArray( vNormal )
            glBindBuffer (GL_ARRAY_BUFFER, B.nbuffer)
            glVertexAttribPointer( vNormal, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p (0))
                
        # texture coord data
        if( B.tSize > 0  ) :
            vTexCoord = glGetAttribLocation( program, "vTexCoord" )
            glEnableVertexAttribArray( vTexCoord )
            glBindBuffer (GL_ARRAY_BUFFER, B.tbuffer)
            glVertexAttribPointer( vTexCoord, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p (0)) 
        
        # return ID
        return vaoID

    def animate1( self ) :
        '''
        function for animating the ball
        '''
        if( self.animating1) :
            self.rotBall += 2.0
            if(self.transBall >= 0.37):
                self.transBall = self.transBall - 0.03
                self.display()
            else:
                self.animating1 = False
                self.animating2 = True

        if (self.animating2):
            if (self.transBall <= 1.2):
                self.rotBall -= 0.5
                self.transBall = self.transBall + 0.0045
                self.display()
            elif (self.transBall <= 1.4 and self.transBall > 1.2):
                self.rotBall -= 0.3
                self.transBall = self.transBall + 0.002
                self.display()
            else:
                self.animating2 = False

    def display( self ) :
        '''
        function for displaying
        '''
        
        # clear the frame buffer
        glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    
        # first the quad
        glUseProgram (self.tshader)

        # set up viewing and projection parameters
        self.view.setUpFrustum( self.tshader )

        # set up the texture information
        self.tex.setUpTexture( self.tshader )

        # set up the camera
        self.view.setUpCamera( self.tshader, 0.2, 3.0, 6.5, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0 )

        # set up transformations for the quad
        self.view.setUpTransforms( self.tshader, 6.5, 2.2, 1.5, -65.0, 0.0, 0.75, -0.1, -2.1, -1.5)

        # draw it
        glBindVertexArray (self.qVao)
        glDrawArrays(GL_TRIANGLES, 0, self.quadBuffers.numElements)

        # now the ball
        glUseProgram( self.pshader )

        # set up viewing and projection parameters
        self.view.setUpFrustum( self.pshader )
    
        # set up the ball shading information
        self.light.setUpPhong( self.pshader )
    
        # set up the camera
        self.view.setUpCamera( self.pshader, 0.2, 3.0, 6.5, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)

        # set up transforms
        self.view.setUpTransforms( self.pshader, 1.5, 1.5, 1.5, 0.0, 0.0, self.rotBall, self.transBall, -1.0, -1.0 )
                
        # draw it
        glBindVertexArray (self.tVao)
        glDrawArrays(GL_TRIANGLES, 0, self.ballBuffers.numElements)

        # now the base
        glUseProgram(self.bshader)

        # set up viewing and projection parameters
        self.view.setUpFrustum(self.bshader)

        # set up the base shading information
        self.baselight.setUpBase(self.bshader)

        # set up the camera
        self.view.setUpCamera(self.bshader, 0.2, 3.0, 6.5, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)

        # set up transforms
        self.view.setUpTransforms(self.bshader, 2.0, 0.8, 2.0, -10.0, 5.0, 0.0, -1.0, -1.0, -1.5)

        # draw it
        glBindVertexArray(self.bVao)
        glDrawArrays(GL_TRIANGLES, 0, self.baseBuffers.numElements)

        # now the stand
        glUseProgram(self.sshader)

        # set up viewing and projection parameters
        self.view.setUpFrustum(self.sshader)

        # set up the stand shading information
        self.standlight.setUpStand(self.sshader)

        # set up the camera
        self.view.setUpCamera(self.sshader, 0.2, 3.0, 6.5, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)

        # set up transforms
        self.view.setUpTransforms(self.sshader, 2.5, 0.5, 0.2, -7.0, 30.0, 90.0, -1.1, 0.3, -1.4)

        # draw it
        glBindVertexArray(self.sVao)
        glDrawArrays(GL_TRIANGLES, 0, self.standBuffers.numElements)

        # now the tilt
        glUseProgram(self.lshader)

        # set up viewing and projection parameters
        self.view.setUpFrustum(self.lshader)

        # set up the tilt shading information
        self.tiltlight.setUpTilt(self.lshader)

        # set up the camera
        self.view.setUpCamera(self.lshader, 0.2, 3.0, 6.5, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)

        # set up transforms
        self.view.setUpTransforms(self.lshader, 2.0, 0.5, 0.2, 30.0, 30.0, 35.0, -0.4, 2.1, -1.6)

        # draw it
        glBindVertexArray(self.lVao)
        glDrawArrays(GL_TRIANGLES, 0, self.tiltBuffers.numElements)

        # now the lamp
        glUseProgram(self.cshader)

        # set up viewing and projection parameters
        self.view.setUpFrustum(self.cshader)

        # set up the lamp shading information
        self.lamplight.setUpLamp(self.cshader)

        # set up the camera
        self.view.setUpCamera(self.cshader, 0.2, 3.0, 6.5, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)

        # set up transforms
        self.view.setUpTransforms(self.cshader, 2.0, 2.0, 1.5, 70.0, 30.0, 30.0, 0.4, 2.4, -1.8)

        # draw it
        glBindVertexArray(self.cVao)
        glDrawArrays(GL_TRIANGLES, 0, self.lampBuffers.numElements)

        # Swap the buffers
        glutSwapBuffers()


    # main function
    def main(self):
    
        glutInit()
        glutInitDisplayMode(GLUT_RGBA|GLUT_ALPHA|GLUT_DOUBLE|GLUT_DEPTH|GLUT_3_2_CORE_PROFILE)
        glutInitWindowSize(512,512)
        glutCreateWindow(b"Transformation Demo")
    
        self.init()
    
        glutDisplayFunc(self.display)
        glutIdleFunc(self.animate1)
        
        glutMainLoop()
        
        self.dispose()


if __name__ == '__main__':
    luxoJr().main()
