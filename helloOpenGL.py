'''
Created on Mar 12, 2014

@author: Srinivas Sridharan
'''
from OpenGL.GL import *
from OpenGL.GLUT import *
from shaderSetup import shaderSetup
from numpy import array, arange



class helloOpenGL(object):

    '''
    Number of Vertices
    '''
    nVerts = 30
    
    '''
    Element Data as numpy array Type - uint16
    '''
    elems = array ([0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
                15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],dtype='uint16')

    '''
    Vertex Data as numpy array Type - float32
    '''
    datapoints = array([0.25, -0.75, 0.0, 1.0,
         0.50, -0.75, 0.0, 1.0,
         0.25,  0.15, 0.0, 1.0,

         0.50, -0.75, 0.0, 1.0,
         0.50,  0.15, 0.0, 1.0,
         0.25,  0.15, 0.0, 1.0,

         0.25,  0.25, 0.0, 1.0,
         0.50,  0.25, 0.0, 1.0,
         0.25,  0.50, 0.0, 1.0,

         0.50,  0.25, 0.0, 1.0,
         0.50,  0.50, 0.0, 1.0,
         0.25,  0.50, 0.0, 1.0,

        -0.25, -0.75, 0.0, 1.0,
         0.00, -0.75, 0.0, 1.0,
        -0.25,  0.75, 0.0, 1.0,

         0.00, -0.75, 0.0, 1.0,
         0.00,  0.75, 0.0, 1.0,
        -0.25,  0.75, 0.0, 1.0,

        -0.75, -0.75, 0.0, 1.0,
        -0.50, -0.75, 0.0, 1.0,
        -0.75,  0.75, 0.0, 1.0,

        -0.50, -0.75, 0.0, 1.0,
        -0.50,  0.75, 0.0, 1.0,
        -0.75,  0.75, 0.0, 1.0,

        -0.50, -0.12, 0.0, 1.0,
        -0.25, -0.12, 0.0, 1.0,
        -0.50,  0.12, 0.0, 1.0,

        -0.25, -0.12, 0.0, 1.0,
        -0.25,  0.12, 0.0, 1.0,
        -0.50,  0.12, 0.0, 1.0],dtype='float32')                                  

    '''
    Color 1 Data as numpy array Type - float32
    '''
    colors1 = array([0.00, 1.00, 0.00, 1.0,   0.00, 1.00, 0.00, 1.0,   0.00, 0.28, 0.72, 1.0,
                     0.00, 1.00, 0.00, 1.0,   0.00, 0.28, 0.72, 1.0,   0.00, 0.28, 0.72, 1.0,
                     0.00, 0.20, 0.80, 1.0,   0.00, 0.20, 0.80, 1.0,   0.00, 0.00, 1.00, 1.0,
                     0.00, 0.20, 0.80, 1.0,   0.00, 0.00, 1.00, 1.0,   0.00, 0.00, 1.00, 1.0,
                     1.00, 0.00, 0.00, 1.0,   1.00, 0.00, 0.00, 1.0,   1.00, 0.00, 0.00, 1.0,
                     1.00, 0.00, 0.00, 1.0,   1.00, 0.00, 0.00, 1.0,   1.00, 0.00, 0.00, 1.0,
                     1.00, 1.00, 0.00, 1.0,   1.00, 1.00, 0.00, 1.0,   1.00, 1.00, 0.00, 1.0,
                     1.00, 1.00, 0.00, 1.0,   1.00, 1.00, 0.00, 1.0,   1.00, 1.00, 0.00, 1.0,
                     1.00, 1.00, 0.00, 1.0,   1.00, 0.00, 0.00, 1.0,   1.00, 1.00, 0.00, 1.0,
                     1.00, 0.00, 0.00, 1.0,   1.00, 0.00, 0.00, 1.0,   1.00, 1.00, 0.00, 1.0],dtype='float32')

    '''
    Color 2 Data as numpy array Type - float32
    '''
    colors2 = array([1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,
                     1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,
                     1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,
                     1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,
                     1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,
                     1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,
                     1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,
                     1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,
                     1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,
                     1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0,   1.00, 1.00, 1.00, 1.0],dtype='float32')


    #program ID returned from Shader Program
    shaderProgID = None
    bufferInt = False

    '''
    Initializing Vertex Array IDs
    '''
    HelloColor = 0
    HelloWhite = 0
    
    #constructor
    def __init__(self, params):
        '''
        Constructor
        '''
        self.counter = 0
        self.dataSize = self.nVerts * 4 * 4
        self.elemSize = self.nVerts * 2
        self.colorSize1 = self.dataSize
        self.colorSize2 = self.dataSize


    #Just implemented as in Java file, don't think its used
    def errorCheck(self):
        errorCode = glGetError()
        
        if  errorCode == GL_NO_ERROR:
            print ("Everything is going well")
        else:
            print ("Problem with error ", errorCode)
            raise Exception("GL Error Detected ", errorCode)

    #Display function        
    def display(self):
        
        #Clear the window and the frame buffers
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
             
        #Bind appropriate vertex array
        if (self.counter & 1) == 0:
            glBindVertexArray (self.HelloColor)
        else:
            glBindVertexArray (self.HelloWhite)

        # draw your shapes
        glDrawArrays(GL_TRIANGLES, 0, self.nVerts)
        
        #Swap the buffers
        glutSwapBuffers()
    
    '''
    * Creates the buffer given the target, data and size
    '''
    def makeBuffer(self,target,data,size):
        #Generate and Bind vertex buffer and load vertex data
        buffer = glGenBuffers(1)
        glBindBuffer(target, buffer)
        glBufferData(target, size, data, GL_STATIC_DRAW)
        return buffer

    
    '''
    * Creates VAO for given set of objects.  Returns the VAO ID
    '''
    def createVAO (self, colorArray, colorSize) :
        
        # Get yourself an ID
        vaoID = GLuint(0)
        glGenVertexArrays(1, vaoID)
        
        # You'll need the correct program to get the location of the vertex
        # attributes
        glUseProgram(self.shaderProgID)
        vPosition = glGetAttribLocation(self.shaderProgID,"vPosition")
        vColor = glGetAttribLocation(self.shaderProgID, "vColor")
        
        # Bind the vertex array object
        glBindVertexArray (vaoID)
        
        # Make and fill your buffer
        # We'll combine vertex data and color in same buffer (vertex first then color)
        # but could have just as well had separate buffers for each
        self.makeBuffer (GL_ARRAY_BUFFER, None , self.dataSize + colorSize)
        glBufferSubData( GL_ARRAY_BUFFER, 0, self.dataSize, self.datapoints )
        glBufferSubData( GL_ARRAY_BUFFER, self.dataSize, colorSize, colorArray )
        
        # set buffers to correct vertext attribute
        glEnableVertexAttribArray(vPosition)
        glVertexAttribPointer(vPosition,4,GL_FLOAT,GL_FALSE,0,ctypes.c_void_p(0))
        glEnableVertexAttribArray(vColor)
        glVertexAttribPointer(vColor,4,GL_FLOAT,GL_FALSE,0, ctypes.c_void_p (self.dataSize))
        
        # Make and fill your elements array
        self.makeBuffer(GL_ELEMENT_ARRAY_BUFFER, self.elems, self.elemSize)
        
        # return your ID
        return vaoID
    
    
    
    
    #Initialization function         
    def init(self):
        
        #Read and compile the shaders
        myShaders = shaderSetup(None)
        self.shaderProgID = myShaders.readAndCompile("shader.vert", "shader.frag")
        
        #Check the program ID
        if self.shaderProgID <= 0:
            print ("Error setting up program ID")
            raise Exception("Error setting up program ID", "fatal")


        #Other GL initialization
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glCullFace(GL_BACK)
        glFrontFace(GL_CCW)
        glClearColor(1.0,1.0,1.0,1.0)
        glDepthFunc(GL_LEQUAL)
        glClearDepth(1.0)

        # create the vertex array objects for the two screen
        self.HelloColor = self.createVAO (self.colors1, self.colorSize1)
        self.HelloWhite = self.createVAO (self.colors2, self.colorSize2)

    '''
     * Notifies the listener to perform the release of all OpenGL 
     * resources per GLContext, such as memory buffers and GLSL 
     * programs.
    '''    
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
    
    def keyPressed(self,*args):

        #Get the key that was pressed
        key = str(args[0].decode())

        if(key == '1'):
            self.counter = 0
        elif(key == '2'):
            self.counter = 1
        elif(key == 'q' or key == 'Q'):
            sys.exit()
        elif(args[0] == '\033'): #Escape character
            sys.exit()

        self.display()
    
    def main(self):
        
        glutInit()
        glutInitDisplayMode(GLUT_RGBA|GLUT_ALPHA|GLUT_DOUBLE|GLUT_DEPTH|GLUT_3_2_CORE_PROFILE)
        glutInitWindowSize(512,512)
        glutCreateWindow(b"Hello World OpenGL")
        
        self.init()
        
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutKeyboardFunc(self.keyPressed)
        
        glutMainLoop()
        
        self.dispose()
    
if __name__ == "__main__":
    helloOpenGL(None).main()
