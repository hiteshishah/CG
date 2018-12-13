# Copyright(c) Max Kolosov 2010 maxkolosov@inbox.ru
# http://vosolok2008.narod.ru
# BSD license

__version__ = '0.1'
__versionTime__ = '2010-02-12'
__author__ = 'Max Kolosov <maxkolosov@inbox.ru>'

import os, sys, pysoil
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_title = 'python OpenGL FPS exampl'
ESCAPE = '\033'
#~ glut_cursor = GLUT_CURSOR_NONE
glut_cursor = GLUT_CURSOR_FULL_CROSSHAIR
enable_cull_face = False
cull_face = GL_FRONT# or GL_BACK or GL_FRONT_AND_BACK
w_width = 640.0
w_height = 480.0
center_width = w_width / 2
center_height = w_height / 2
window = 0
texture = 0
quadratic = 0
up_down = 0
left_right = 0
speed = 0.8
speed_rotate = 5.0
align_camera = 90.0
z_near = 0.1
z_far = 1000.0

sky_diameter = 400.0

images_path = 'imgs/'
max_texture_size = 2
user_texture_size = 32
old_mouse_dx, old_mouse_dy, mouse_dx, mouse_dy = 0.0, 0.0, 0.0, 0.0
volume_heigth = 2.0
volume_attr = {'x1':-100.0, 'x2':100.0, 'y1':-1.0, 'y2':volume_heigth, 'z1':-100.0, 'z2':100.0}
texture_attr = {'x1':0.0, 'x2':100.0, 'y1':0.0, 'y2':volume_heigth, 'z1':0.0, 'z2':100.0}
textures = {'face':0, 'back':1, 'left':2, 'right':3, 'top':4, 'bottom':5, 'sky':6}

def convert_arr_to_str(value, format = '%.2f'):
	result = []
	for item in value:
		result.append(format%item)
	return result

def LoadTextures():
	global images_path, textures, max_texture_size, user_texture_size
	print 'Loading Textures ...'
	for texture_name in textures.iterkeys():
		texture_file_name = images_path + texture_name + '.jpg'
		image = None
		if not os.path.isfile(texture_file_name):
			print 'Texture file', texture_file_name, 'not exists'
			texture_file_name = images_path + texture_name + '.png'
			if not os.path.isfile(texture_file_name):
				print 'Texture file', texture_file_name, 'not exists'
				continue
		print 'Load Texture form ' + texture_file_name
		textures[texture_name] = pysoil.SOIL_load_OGL_texture(
			texture_file_name,
			pysoil.SOIL_LOAD_AUTO,
			pysoil.SOIL_CREATE_NEW_ID,
			pysoil.SOIL_FLAG_POWER_OF_TWO|
			pysoil.SOIL_FLAG_MIPMAPS|
			pysoil.SOIL_FLAG_MULTIPLY_ALPHA|
			pysoil.SOIL_FLAG_INVERT_Y|
			pysoil.SOIL_FLAG_DDS_LOAD_DIRECT|
			pysoil.SOIL_FLAG_NTSC_SAFE_RGB)
		glBindTexture(GL_TEXTURE_2D, textures[texture_name])
		#~ glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

def InitGL(Width, Height): # call after OpenGL window is created.
	global quadratic, cull_face, w_width, w_height, align_camera, z_near, z_far, max_texture_size, user_texture_size
	max_texture_size = glGetIntegerv(GL_MAX_TEXTURE_SIZE)
	if user_texture_size > max_texture_size:
		user_texture_size = max_texture_size
	print gluGetString(GLU_VERSION), gluGetString(GLU_EXTENSIONS)
	print 'GL_MAX_TEXTURE_SIZE:', max_texture_size
	print 'GL_MAX_PIXEL_MAP_TABLE:', glGetIntegerv(GL_MAX_PIXEL_MAP_TABLE)
	print 'front and back buffers exist:', bool(glGetBooleanv(GL_DOUBLEBUFFER))
	print 'left and right buffers exist:', bool(glGetBooleanv(GL_STEREO))
	print 'Range (low to high) of antialiased point sizes:', glGetFloatv(GL_POINT_SIZE_RANGE)
	print 'Antialiased point size granularity:', glGetFloatv(GL_POINT_SIZE_GRANULARITY)
	print 'Range (low to high) of antialiased line sizes:', glGetFloatv(GL_LINE_WIDTH_RANGE)
	print 'Antialiased line size granularity:', glGetFloatv(GL_LINE_WIDTH_GRANULARITY)
	w_width, w_height = Width, Height

	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE)

	LoadTextures()

	quadratic = gluNewQuadric()
	gluQuadricNormals(quadratic, GLU_SMOOTH)		# Create Smooth Normals (NEW) 
	gluQuadricTexture(quadratic, GL_TRUE)			# Create Texture Coords (NEW) 

	glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
	glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
	glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
	glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
	if not glIsEnabled(GL_CULL_FACE) and enable_cull_face:
		glEnable(GL_CULL_FACE)
		glCullFace(cull_face)
	if not glIsEnabled(GL_TEXTURE_2D):
		glEnable(GL_TEXTURE_2D)
	glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading

def ReSizeGLScene(Width, Height):
	global w_width, w_height, align_camera, z_near, z_far, center_width, center_height
	if Height == 0:# Prevent A Divide By Zero If The Window Is Too Small 
		Height = 1
	w_width, w_height = Width, Height
	center_width = w_width / 2
	center_height = w_height / 2
	glViewport(0, 0, w_width, w_height)# Reset The Current Viewport And Perspective Transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(align_camera, float(w_width)/float(w_height), z_near, z_far)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def DrawGLScene():
	global quadratic, textures, up_down, left_right, mouse_dx, mouse_dy, center_width, center_height, sky_diameter
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)	# Clear The Screen And The Depth Buffer
	# Start Drawing The Volume
	# Front Face (note that the texture's corners have to match the quad's corners)
	#~ glEnable(GL_TEXTURE_2D)
	glBindTexture(GL_TEXTURE_2D, textures['face'])
	glBegin(GL_QUADS)
	glTexCoord2f(texture_attr['x1'], texture_attr['y1']); glVertex3f(volume_attr['x1'], volume_attr['y1'],  volume_attr['z2'])	# Bottom Left Of The Texture and Quad
	glTexCoord2f(texture_attr['x2'], texture_attr['y1']); glVertex3f(volume_attr['x2'], volume_attr['y1'],  volume_attr['z2'])	# Bottom Right Of The Texture and Quad
	glTexCoord2f(texture_attr['x2'], texture_attr['y2']); glVertex3f(volume_attr['x2'],  volume_attr['y2'],  volume_attr['z2'])	# Top Right Of The Texture and Quad
	glTexCoord2f(texture_attr['x1'], texture_attr['y2']); glVertex3f(volume_attr['x1'],  volume_attr['y2'],  volume_attr['z2'])	# Top Left Of The Texture and Quad
	glEnd()
	# Back Face
	glBindTexture(GL_TEXTURE_2D, textures['back'])
	glBegin(GL_QUADS)
	glTexCoord2f(texture_attr['x2'], texture_attr['y1']); glVertex3f(volume_attr['x1'], volume_attr['y1'],  volume_attr['z1'])	# Bottom Right Of The Texture and Quad
	glTexCoord2f(texture_attr['x2'], texture_attr['y2']); glVertex3f(volume_attr['x1'], volume_attr['y2'],  volume_attr['z1'])	# Top Right Of The Texture and Quad
	glTexCoord2f(texture_attr['x1'], texture_attr['y2']); glVertex3f(volume_attr['x2'], volume_attr['y2'],  volume_attr['z1'])	# Top Left Of The Texture and Quad
	glTexCoord2f(texture_attr['x1'], texture_attr['y1']); glVertex3f(volume_attr['x2'], volume_attr['y1'],  volume_attr['z1'])	# Bottom Left Of The Texture and Quad
	glEnd()
	# Top Face
	glBindTexture(GL_TEXTURE_2D, textures['top'])
	glBegin(GL_QUADS)
	glTexCoord2f(texture_attr['x1'], texture_attr['z2']); glVertex3f(volume_attr['x1'], volume_attr['y2'],  volume_attr['z1'])	# Top Left Of The Texture and Quad
	glTexCoord2f(texture_attr['x1'], texture_attr['z1']); glVertex3f(volume_attr['x1'], volume_attr['y2'],  volume_attr['z2'])	# Bottom Left Of The Texture and Quad
	glTexCoord2f(texture_attr['x2'], texture_attr['z1']); glVertex3f(volume_attr['x2'], volume_attr['y2'],  volume_attr['z2'])	# Bottom Right Of The Texture and Quad
	glTexCoord2f(texture_attr['x2'], texture_attr['z2']); glVertex3f(volume_attr['x2'], volume_attr['y2'],  volume_attr['z1'])	# Top Right Of The Texture and Quad
	glEnd()
	# Bottom Face       
	glBindTexture(GL_TEXTURE_2D, textures['bottom'])
	glBegin(GL_QUADS)
	glTexCoord2f(texture_attr['x2'], texture_attr['z2']); glVertex3f(volume_attr['x1'], volume_attr['y1'],  volume_attr['z1'])	# Top Right Of The Texture and Quad
	glTexCoord2f(texture_attr['x1'], texture_attr['z2']); glVertex3f(volume_attr['x2'], volume_attr['y1'],  volume_attr['z1'])	# Top Left Of The Texture and Quad
	glTexCoord2f(texture_attr['x1'], texture_attr['z1']); glVertex3f(volume_attr['x2'], volume_attr['y1'],  volume_attr['z2'])	# Bottom Left Of The Texture and Quad
	glTexCoord2f(texture_attr['x2'], texture_attr['z1']); glVertex3f(volume_attr['x1'], volume_attr['y1'],  volume_attr['z2'])	# Bottom Right Of The Texture and Quad
	glEnd()
	# Right face
	glBindTexture(GL_TEXTURE_2D, textures['right'])
	glBegin(GL_QUADS)
	glTexCoord2f(texture_attr['x2'], texture_attr['y1']); glVertex3f(volume_attr['x2'], volume_attr['y1'],  volume_attr['z1'])	# Bottom Right Of The Texture and Quad
	glTexCoord2f(texture_attr['x2'], texture_attr['y2']); glVertex3f(volume_attr['x2'], volume_attr['y2'],  volume_attr['z1'])	# Top Right Of The Texture and Quad
	glTexCoord2f(texture_attr['x1'], texture_attr['y2']); glVertex3f(volume_attr['x2'], volume_attr['y2'],  volume_attr['z2'])	# Top Left Of The Texture and Quad
	glTexCoord2f(texture_attr['x1'], texture_attr['y1']); glVertex3f(volume_attr['x2'], volume_attr['y1'],  volume_attr['z2'])	# Bottom Left Of The Texture and Quad
	glEnd()
	# Left Face
	glBindTexture(GL_TEXTURE_2D, textures['left'])
	glBegin(GL_QUADS)
	glTexCoord2f(texture_attr['x1'], texture_attr['y1']); glVertex3f(volume_attr['x1'], volume_attr['y1'],  volume_attr['z1'])	# Bottom Left Of The Texture and Quad
	glTexCoord2f(texture_attr['x2'], texture_attr['y1']); glVertex3f(volume_attr['x1'], volume_attr['y1'],  volume_attr['z2'])	# Bottom Right Of The Texture and Quad
	glTexCoord2f(texture_attr['x2'], texture_attr['y2']); glVertex3f(volume_attr['x1'], volume_attr['y2'],  volume_attr['z2'])	# Top Right Of The Texture and Quad
	glTexCoord2f(texture_attr['x1'], texture_attr['y2']); glVertex3f(volume_attr['x1'], volume_attr['y2'],  volume_attr['z1'])	# Top Left Of The Texture and Quad
	glEnd()
	#~ glDisable(GL_TEXTURE_2D)
	# Done Drawing Volume
	# start drawing sky
	#~ glDisable(GL_DEPTH_TEST)
	#~ glColor3d(0, 0, 255)
	glBindTexture(GL_TEXTURE_2D, textures['sky'])
	gluSphere(quadratic, sky_diameter, 32, 32)
	#~ glEnable(GL_DEPTH_TEST)
	# end drawing sky
	#~ gluCylinder(quadratic, 1.0, 1.0, 3.0, 32, 32)
	#~ gluDisk(quadratic, 0.5, 1.5, 32, 32)
	#~ gluSphere(quadratic, 1.3, 32, 32)
	#~ gluCylinder(quadratic, 1.0, 0.0, 3.0, 32, 32)
	#~ gluPartialDisk(quadratic, 0.5, 1.5, 32, 32, 0, 300)
	#~ glTranslatef(5.0, 0.0, 0.0)# move center
	glutSolidTeapot(1.0)
	# moving
	if (up_down or left_right or mouse_dx or mouse_dy) != 0:
		try:
			m = glGetDoublev(GL_MODELVIEW_MATRIX).flatten()
		except AttributeError: # not attr flatten and glGetDoublev return OpenGL.arrays.lists.c_double_Array_4_Array_4
			from itertools import chain
			m = tuple(chain(*glGetDoublev(GL_MODELVIEW_MATRIX)))
		if up_down != 0: # step to forward or backward
			glTranslate(up_down * m[2], up_down * m[6], up_down * m[10])
		if (mouse_dx or mouse_dy) != 0: # rotate to left or right or top or bottom
			try:
				v = glGetDoublev(GL_VIEWPORT).flatten()
			except AttributeError:
				v = tuple(glGetDoublev(GL_VIEWPORT))
			x, y, z = gluUnProject((v[2]-v[0])/2, (v[3]-v[1])/2, 0.0)# camera center in absolute coordinates (x,y,z)
			glTranslate(x, y, z)
			if mouse_dx != 0: # rotate to left or right
				glRotate(mouse_dx, m[1],m[5],m[9])
				mouse_dx = 0.0
			if mouse_dy != 0: # rotate to top or bottom
				glRotate(mouse_dy, m[0],m[4],m[8])
				mouse_dy = 0.0
			glTranslate(-x, -y, -z)
			old_absolute_x, old_absolute_y, old_absolute_z = x, y, z
		if left_right != 0: # step to left or right
			glTranslate(left_right * m[0], left_right * m[4], left_right * m[8])
	else:
		glutIdleFunc(None)
	glutSwapBuffers()

def passive_motion_func(*args):
	global w_width, w_height, old_mouse_dx, old_mouse_dy, mouse_dx, mouse_dy, speed_rotate
	mouse_dx, mouse_dy = args
	new_speed = speed_rotate
	if mouse_dx == old_mouse_dx:
		mouse_dx = 0.0
	else:
		if mouse_dx < old_mouse_dx:
			new_speed *= -1
		old_mouse_dx = mouse_dx
		mouse_dx = new_speed
	if mouse_dy < old_mouse_dy + 1 or mouse_dy > old_mouse_dy - 1:
		mouse_dy = 0.0
	else:
		if mouse_dy < old_mouse_dy:
			new_speed *= -1
		old_mouse_dy = mouse_dy
		mouse_dy = new_speed
	glutIdleFunc(DrawGLScene)

def motion_func(*args):
	# activate event if mouse button pressed
	# x, y = args
	print args

def mouse_func(*args):
	# left = 0, middle = 1, right = 2; up = 0, down = 1
	# button, up_down, x, y = args
	print args

def keyboard_func(*args):
	if args[0] == ESCAPE:
		sys.exit()

def special_func(*args):
	global up_down, left_right
	try:
		v = glGetDoublev(GL_VIEWPORT).flatten()
	except AttributeError:
		v = tuple(glGetDoublev(GL_VIEWPORT))
	x, y, z = gluUnProject((v[2]-v[0])/2, (v[3]-v[1])/2, 0.0)
	if args[0] == 100:# left
		left_right = speed
	elif args[0] == 101:# up
		up_down = speed
	elif args[0] == 102:# right
		left_right = - speed
	elif args[0] == 103:# down
		up_down = - speed
	elif args[0] == 1:# F1
		print 'current absolute(real) position as (x,y,z) is', convert_arr_to_str((x, y, z))
	glutIdleFunc(DrawGLScene)

def special_up_func(*args):
	global up_down, left_right
	if args[0] in (100, 102):# left, right
		left_right = 0
	elif args[0] in (101, 103):# up, down
		up_down = 0

def main():
	global window, window_title, w_width, w_height, glut_cursor
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)# | GLUT_STEREO
	glutInitWindowSize(w_width, w_height)
	glutInitWindowPosition(0, 0)
	window = glutCreateWindow(window_title)
	glutSetCursor(glut_cursor)
	glutDisplayFunc(DrawGLScene)
	#~ glutFullScreen()
	glutIdleFunc(DrawGLScene)
	glutReshapeFunc(ReSizeGLScene)
	glutPassiveMotionFunc(passive_motion_func)
	#~ glutMotionFunc(motion_func)
	#~ glutMouseFunc(mouse_func)
	#~ glutMouseWheelFunc(mouse_wheel_func)#freeglut ('wheel','direction','x','y')
	glutKeyboardFunc(keyboard_func)
	glutSpecialFunc(special_func)
	glutSpecialUpFunc(special_up_func)
	InitGL(w_width, w_height)
	glutMainLoop()

if __name__ == '__main__':
	main()
