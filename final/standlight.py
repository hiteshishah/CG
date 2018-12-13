# standlight.py
#
# Contributor:  Hiteshi Shah (hss7374)
#
# Object for lighting

from OpenGL.GL import *
from numpy import *

class standlight (object):

    # Material properties of the stand of the lamp
    stand_ambient_material_color = [0.2, 0.2, 0.2, 1.0]
    stand_diffuse_material_color = [0.5, 0.5, 0.5, 1.0]
    stand_specular_material_color = [0.5, 0.5, 0.5, 1.0]

    # Reflective characteristics of the stand of the lamp
    stand_ambient_reflection_coefficient = 0.5
    stand_diffuse_reflection_coefficient = 0.7
    stand_specular_reflection_coefficient = 1.0
    stand_specular_exponent = 1.0

    # Properties of the light source
    stand_light_color = [1.0, 1.0, 1.0, 1.0]
    stand_light_position = [5.0, 8.0, 10.0, 1.0]

    # Ambient light in the scene
    stand_ambient_light = [0.5, 0.5, 0.5, 1.0]

    def setUpStand( self,  program ) :
        '''
        function to set up the lighting, material, and shading parameters for the stand shader
        :param program: The ID of an OpenGL (GLSL) shader program to which parameter values are to be sent
        '''

        glUniform4fv(glGetUniformLocation(program, "stand_light_color"), 1, self.stand_light_color)
        glUniform4fv(glGetUniformLocation(program, "stand_light_position"), 1, self.stand_light_position)
        glUniform4fv(glGetUniformLocation(program, "stand_ambient_material_color"), 1, self.stand_ambient_material_color)
        glUniform4fv(glGetUniformLocation(program, "stand_diffuse_material_color"), 1, self.stand_diffuse_material_color)
        glUniform4fv(glGetUniformLocation(program, "stand_specular_material_color"), 1, self.stand_specular_material_color)
        glUniform4fv(glGetUniformLocation(program, "stand_ambient_light"), 1, self.stand_ambient_light)

        glUniform1f(glGetUniformLocation(program, "stand_ambient_reflection_coefficient"), self.stand_ambient_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "stand_diffuse_reflection_coefficient"), self.stand_diffuse_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "stand_specular_reflection_coefficient"), self.stand_specular_reflection_coefficient)
        glUniform1f(glGetUniformLocation(program, "stand_specular_exponent"), self.stand_specular_exponent)
