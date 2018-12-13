import sys

from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import array, arange
from teapot import teapot
from quad import quad
from shaderSetup import shaderSetup
from viewParams import viewParams
from textures import *
from lighting import *
from simpleShape import *
from bufferSet import *

class textingMain (object) :
    
    # our viewparams
    view = viewParams ()
    
    # lighting and textures
    tex = textures ()
    light = lighting()

    # dimensions of the drawing window
    w_width  = 600
    w_height = 600

    # buffer information
    quadBuffers = bufferSet(None)
    teapotBuffers = bufferSet(None)

    # animation flag
    animating = False

    # initial rotations
    rotQuad = 0.0
    rotTeapot = 0.0

    # program IDs...for program and parameters
    pshader = GLuint (0)
    tshader = GLuint (0)

    # vertex array object
    qVao = GLuint(0)
    tVao = GLuint(0)
    
    
    #
    # initialization
    #
    def init (self):
        
        # Load your textures
        self.tex.loadTexture()

        # Load shaders and verify each
        myShaders = shaderSetup(None)
        self.tshader = myShaders.readAndCompile("texture.vert", "texture.frag")
        if self.tshader <= 0:
            print ("Error setting up Texture shaders")
            raise Exception("Error setting up Texture Shaders", "fatal")
            sys.exit(1)
        
        self.pshader = myShaders.readAndCompile("phong.vert", "phong.frag")
        if self.pshader <= 0:
            print ("Error setting up Phong shaders")
            raise Exception("Error setting up Phong Shaders", "fatal")
            sys.exit(1)
                
        # Other OpenGL initialization
        glEnable( GL_DEPTH_TEST )
        glClearColor( 0.0, 0.0, 0.0, 0.0 )
        glPolygonMode( GL_FRONT_AND_BACK, GL_FILL )
        glClearDepth( 1.0 )

        # create teapot
        myShape = teapot()
        myShape.clear()
        myShape.makeTeapot()
        self.tVao = self.createVAO(myShape, self.pshader, self.teapotBuffers )
            
        # create quad
        myShape = quad ()
        myShape.clear()
        myShape.makeQuad()
        self.qVao = self.createVAO(myShape, self.tshader, self.quadBuffers )

            
    '''
    * Creates VAO for given set of objects.  Returns the VAO ID
    '''
    def createVAO (self, shape, program, B) :
        
        # Get yourself an ID
        vaoID = GLuint(0)
        glGenVertexArrays(1, vaoID)
        
        # You'll need the correct program to get the location of the vertex
        # attributes
        glUseProgram(program)
        
        # Bind the vertex array object
        glBindVertexArray (vaoID)
        
        # Make and fill your buffer
        # create the buffers
        B.createBuffers (shape)
        
        # set buffers to correct vertext attribute
        vPosition = glGetAttribLocation(program,"vPosition")
        glEnableVertexAttribArray(vPosition)
        glBindBuffer (GL_ARRAY_BUFFER, B.vbuffer);
        glVertexAttribPointer(vPosition,4,GL_FLOAT,GL_FALSE,0,ctypes.c_void_p(0))
        
        # color data
        if( B.cSize > 0) :
            vColor = glGetAttribLocation( program, "vColor" )
            glEnableVertexAttribArray( vColor )
            glBindBuffer (GL_ARRAY_BUFFER, B.cbuffer);
            glVertexAttribPointer( vColor, 4, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p (0))


        # normal data
        if( B.nSize > 0 ) :
            vNormal = glGetAttribLocation( program, "vNormal" )
            glEnableVertexAttribArray( vNormal )
            glBindBuffer (GL_ARRAY_BUFFER, B.nbuffer);
            glVertexAttribPointer( vNormal, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p (0))
                
        # texture coord data
        if( B.tSize > 0  ) :
            vTexCoord = glGetAttribLocation( program, "vTexCoord" )
            glEnableVertexAttribArray( vTexCoord );
            glBindBuffer (GL_ARRAY_BUFFER, B.tbuffer);
            glVertexAttribPointer( vTexCoord, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p (0)) 
        
        # return your ID
        return vaoID

    #
    # keyboard function
    #
    def keyPressed(self,*args):
    
        #Get the key that was pressed
        key = str(args[0].decode())
    
        # animate
        if(key == 'a'):
            self.animating = True
        
        # stop animating
        elif (key == 's') :
            self.animating = False

        # reset rotations
        elif (key == 'r') :
            self.rotTeapot = 0.0
            self.rotQuad = 0.0
            self.display()

                
        # quit
        elif(key == 'q' or key == 'Q'):
            sys.exit()
        elif(args[0] == '\033'): #Escape character
            sys.exit()
                
    # Animate the objects (maybe)
    def animate( self ) :
        if( self.animating ) :
            self.rotTeapot = self.rotTeapot + 0.5
            self.rotQuad = self.rotQuad + 0.5
            self.display()

    #
    # display function
    #
    def display( self ) :
        
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
        self.view.setUpTransforms( self.tshader, 1.5, 1.5, 1.5, 0.0, self.rotQuad, 0.0, -1.25, 1.0, -1.5)

        # draw it
        glBindVertexArray (self.qVao)
        glDrawArrays(GL_TRIANGLES, 0, self.quadBuffers.numElements)

        # now the teapot
        glUseProgram( self.pshader )

        # set up viewing and projection parameters
        self.view.setUpFrustum( self.pshader )
    
        # set up the Phong shading information
        self.light.setUpPhong( self.pshader )
    
        # set up the camera
        self.view.setUpCamera( self.pshader, 0.2, 3.0, 6.5, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)

        # set up transforms
        self.view.setUpTransforms( self.pshader, 2.0, 2.0, 2.0, 0.0, self.rotTeapot, 0.0, 1.5, 0.5, -1.5 )
                
        # draw it
        glBindVertexArray (self.tVao)
        glDrawArrays(GL_TRIANGLES, 0, self.teapotBuffers.numElements)

        #Swap the buffers
        glutSwapBuffers()


    # main function
    def main(self):
    
        glutInit()
        glutInitDisplayMode(GLUT_RGBA|GLUT_ALPHA|GLUT_DOUBLE|GLUT_DEPTH|GLUT_3_2_CORE_PROFILE)
        glutInitWindowSize(512,512)
        glutCreateWindow(b"Transformation Demo")
    
        self.init()
    
        glutDisplayFunc(self.display)
        glutIdleFunc(self.animate)
        glutKeyboardFunc(self.keyPressed)
        
        glutMainLoop()
        
        self.dispose()


if __name__ == '__main__':
    textingMain().main()
