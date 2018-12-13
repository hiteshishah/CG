# baselight.py
#
# Contributor:  Hiteshi Shah (hss7374)
#
# Object for lighting

from OpenGL.GL import *
from numpy import *

class baselight (object):

    # Material properties of the base of the lamp
    base_ambient_material_color = [0.2, 0.2, 0.2, 1.0]
    base_diffuse_material_color = [0.5, 0.5, 0.5, 1.0]
    base_specular_material_color = [0.5, 0.5, 0.5, 1.0]

    # Reflective characteristics of the base of the lamp
    base_ambient_reflection_coefficient = 0.5
    base_diffuse_reflection_coefficient = 0.7
    base_specular_reflection_coefficient = 1.0
    base_specular_exponent = 10.0

    # Properties of the light source
    base_light_color = [1.0, 1.0, 1.0, 1.0]
    base_light_position = [50.0, -10.0, 6.0, 1.0]

    # Ambient light in the scene
    base_ambient_light = [0.5, 0.5, 0.5, 1.0]

    def setUpBase( self,  program ) :
        '''
        function to set up the lighting, material, and shading parameters for the base shader
        :param program: The ID of an OpenGL (GLSL) shader program to which parameter values are to be sent
        '''

        glUniform4fv(glGetUniformLocation(program, "base_light_color"), 1, self.base_light_color)
        glUniform4fv(glGetUniformLocation(program, "base_light_position"), 1, self.base_light_position)
        glUniform4fv(glGetUniformLocation(program, "base_ambient_material_color"), 1, self.base_ambient_material_color)
        glUniform4fv(glGetUniformLocation(program, "base_diffuse_material_color"), 1, self.base_diffuse_material_color)
        glUniform4fv(glGetUniformLocation(program, "base_specular_material_color"), 1, self.base_specular_material_color)
        glUniform4fv(glGetUniformLocation(program, "base_ambient_light"), 1, self.base_ambient_light)

        glUniform1f(glGetUniformLocation(program, "base_ambient_reflection_coefficient"), self.base_ambient_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "base_diffuse_reflection_coefficient"), self.base_diffuse_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "base_specular_reflection_coefficient"), self.base_specular_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "base_specular_exponent"), self.base_specular_exponent)
