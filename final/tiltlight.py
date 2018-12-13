# tiltlight.py
#
# Contributor:  Hiteshi Shah (hss7374)
#
# Object for lighting

from OpenGL.GL import *
from numpy import *

class tiltlight (object):

    # Material properties of the tilt of the lamp
    tilt_ambient_material_color = [0.2, 0.2, 0.2, 1.0]
    tilt_diffuse_material_color = [0.5, 0.5, 0.5, 1.0]
    tilt_specular_material_color = [0.5, 0.5, 0.5, 1.0]

    # Reflective characteristics of the tilt of the lamp
    tilt_ambient_reflection_coefficient = 0.5
    tilt_diffuse_reflection_coefficient = 0.7
    tilt_specular_reflection_coefficient = 1.0
    tilt_specular_exponent = 50.0

    # Properties of the light source
    tilt_light_color = [0.5, 0.5, 0.5, 1.0]
    tilt_light_position = [8.0, 11.0, 5.0, 1.0]

    # Ambient light in the scene
    tilt_ambient_light = [0.5, 0.5, 0.5, 1.0]

    def setUpTilt( self,  program ) :
        '''
        function to set up the lighting, material, and shading parameters for the tilt shader
        :param program: The ID of an OpenGL (GLSL) shader program to which parameter values are to be sent
        '''

        glUniform4fv(glGetUniformLocation(program, "tilt_light_color"), 1, self.tilt_light_color)
        glUniform4fv(glGetUniformLocation(program, "tilt_light_position"), 1, self.tilt_light_position)
        glUniform4fv(glGetUniformLocation(program, "tilt_ambient_material_color"), 1, self.tilt_ambient_material_color)
        glUniform4fv(glGetUniformLocation(program, "tilt_diffuse_material_color"), 1, self.tilt_diffuse_material_color)
        glUniform4fv(glGetUniformLocation(program, "tilt_specular_material_color"), 1, self.tilt_specular_material_color)
        glUniform4fv(glGetUniformLocation(program, "tilt_ambient_light"), 1, self.tilt_ambient_light)

        glUniform1f(glGetUniformLocation(program, "tilt_ambient_reflection_coefficient"), self.tilt_ambient_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "tilt_diffuse_reflection_coefficient"), self.tilt_diffuse_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "tilt_specular_reflection_coefficient"), self.tilt_specular_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "tilt_specular_exponent"), self.tilt_specular_exponent)
