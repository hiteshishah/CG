# Textures.py
#
# Contributor:  Hiteshi Shah (hss7374)
#
# Object for texture mapping

from OpenGL.GL import *
import sys, ctypes, platform
from numpy import *
from pysoil import *

class textures (object):

    # Reflective characteristics of the teapot and the quad
    ambient_reflection_coefficient = 0.5
    diffuse_reflection_coefficient = 0.7
    specular_reflection_coefficient = 1.0
    specular_exponent = 10.0

    # Properties of the light source
    light_color = [1.0, 1.0, 0.0, 1.0]
    light_position = [0.0, 5.0, 2.0, 1.0]

    # Ambient light in the scene
    ambient_light = [0.5, 0.5, 0.5, 1.0]

    def loadTexture( self ) :
        '''
        function to load texture data for the GPU
        '''

        glActiveTexture(GL_TEXTURE0)
        frontTexture = SOIL_load_OGL_texture("smiley2.png",
                                        SOIL_LOAD_AUTO,
                                        SOIL_CREATE_NEW_ID,
                                        SOIL_FLAG_MIPMAPS | SOIL_FLAG_TEXTURE_REPEATS)
        glBindTexture(GL_TEXTURE_2D, frontTexture)

        glActiveTexture(GL_TEXTURE1)
        backTexture = SOIL_load_OGL_texture("frowny2.png",
                                            SOIL_LOAD_AUTO,
                                            SOIL_CREATE_NEW_ID,
                                            SOIL_FLAG_MIPMAPS | SOIL_FLAG_TEXTURE_REPEATS)
        glBindTexture(GL_TEXTURE_2D, backTexture)


    def setUpTexture( self, program ) :
        '''
        function to set up the parameters for texture use
        :param program: The ID of an OpenGL (GLSL) shader program to which parameter values are to be sent
        '''

        glUseProgram(program)
        glUniform1i(glGetUniformLocation(program, "frontTexture"), 0)
        glUniform1i(glGetUniformLocation(program, "backTexture"), 1)
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D_ARRAY, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        glUniform4fv(glGetUniformLocation(program, "light_color"), 1, self.light_color)
        glUniform4fv(glGetUniformLocation(program, "light_position"), 1, self.light_position)
        glUniform4fv(glGetUniformLocation(program, "ambient_light"), 1, self.ambient_light)

        glUniform1f(glGetUniformLocation(program, "ambient_reflection_coefficient"),
                    self.ambient_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "diffuse_reflection_coefficient"),
                    self.diffuse_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "specular_reflection_coefficient"),
                    self.specular_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "specular_exponent"), self.specular_exponent)