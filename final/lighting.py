# lighting.py
#
# Contributor:  Hiteshi Shah (hss7374)
#
# Object for lighting

from OpenGL.GL import *
from numpy import *

class lighting (object):

    # Material properties of the ball
    ambient_material_color = [0.3, 0.3, 0.0, 1.0]
    diffuse_material_color = [1.0, 0.88, 0.0, 1.0]
    specular_material_color = [0.5, 0.5, 0.0, 1.0]

    # Reflective characteristics of the ball
    ambient_reflection_coefficient = 0.7
    diffuse_reflection_coefficient = 0.5
    specular_reflection_coefficient = 1.0
    specular_exponent = 10.0

    # Properties of the light source
    light_color = [1.0, 1.0, 0.0, 1.0]
    light_position = [-1.0, 1.0, 0.0, 1.0]

    # Ambient light in the scene
    ambient_light = [1.0, 1.0, 0.0, 1.0]

    def setUpPhong( self,  program ) :
        '''
        function to set up the lighting, material, and shading parameters for the ball shader
        :param program: The ID of an OpenGL (GLSL) shader program to which parameter values are to be sent
        '''

        glUniform4fv(glGetUniformLocation(program, "light_color"), 1, self.light_color)
        glUniform4fv(glGetUniformLocation(program, "light_position"), 1, self.light_position)
        glUniform4fv(glGetUniformLocation(program, "ambient_material_color"), 1, self.ambient_material_color)
        glUniform4fv(glGetUniformLocation(program, "diffuse_material_color"), 1, self.diffuse_material_color)
        glUniform4fv(glGetUniformLocation(program, "specular_material_color"), 1, self.specular_material_color)
        glUniform4fv(glGetUniformLocation(program, "ambient_light"), 1, self.ambient_light)

        glUniform1f(glGetUniformLocation(program, "ambient_reflection_coefficient"), self.ambient_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "diffuse_reflection_coefficient"), self.diffuse_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "specular_reflection_coefficient"), self.specular_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "specular_exponent"), self.specular_exponent)
