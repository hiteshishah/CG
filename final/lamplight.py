# lamplight.py
#
# Contributor:  Hiteshi Shah (hss7374)
#
# Object for lighting

from OpenGL.GL import *
from numpy import *

class lamplight (object):

    # Material properties of the cone of the lamp
    lamp_ambient_material_color = [0.2, 0.2, 0.2, 1.0]
    lamp_diffuse_material_color = [0.5, 0.5, 0.5, 1.0]
    lamp_specular_material_color = [0.5, 0.5, 0.5, 1.0]

    # Reflective characteristics of the cone of the lamp
    lamp_ambient_reflection_coefficient = 0.5
    lamp_diffuse_reflection_coefficient = 0.7
    lamp_specular_reflection_coefficient = 1.0
    lamp_specular_exponent = 30.0

    # Properties of the light source
    lamp_light_color = [2.5, 2.5, 2.5, 1.0]
    lamp_light_position = [50.0, -50.0, 0.0, 1.0]

    # Ambient light in the scene
    lamp_ambient_light = [0.5, 0.5, 0.5, 1.0]

    def setUpLamp( self,  program ) :
        '''
        function to set up the lighting, material, and shading parameters for the lamp shader
        :param program: The ID of an OpenGL (GLSL) shader program to which parameter values are to be sent
        '''

        glUniform4fv(glGetUniformLocation(program, "lamp_light_color"), 1, self.lamp_light_color)
        glUniform4fv(glGetUniformLocation(program, "lamp_light_position"), 1, self.lamp_light_position)
        glUniform4fv(glGetUniformLocation(program, "lamp_ambient_material_color"), 1, self.lamp_ambient_material_color)
        glUniform4fv(glGetUniformLocation(program, "lamp_diffuse_material_color"), 1, self.lamp_diffuse_material_color)
        glUniform4fv(glGetUniformLocation(program, "lamp_specular_material_color"), 1, self.lamp_specular_material_color)
        glUniform4fv(glGetUniformLocation(program, "lamp_ambient_light"), 1, self.lamp_ambient_light)

        glUniform1f(glGetUniformLocation(program, "lamp_ambient_reflection_coefficient"), self.lamp_ambient_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "lamp_diffuse_reflection_coefficient"), self.lamp_diffuse_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "lamp_specular_reflection_coefficient"), self.lamp_specular_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "lamp_specular_exponent"), self.lamp_specular_exponent)
