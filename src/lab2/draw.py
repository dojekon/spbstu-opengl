import cameraMotion as camera
import textureLoader as texture
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

polygon_number = 64

light_pos = [0., 0., 4., 1.]
light_const_attenuation = 0.8
light_color = [0.8, 0.8, 0.8]
light_angle = 0

def draw_light():
    glRotatef(light_angle, 1., 0., 0.)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

    # If the light is positional, rather than directional, its intensity is attenuated by the reciprocal of the sum
    # of the constant factor, the linear factor times the distance between the light and the vertex being lighted,
    # and the quadratic factor times the square of the same distance
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, light_const_attenuation)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.1)

# Полупрозрачный куб
cube_pos = (0.9, 0.8, 0.8)

def draw_cube():
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.2, 0.2, 0.4, 0.9))
    glutSolidCube(2)

# Отполированный конус
cone_height, cone_radius = 2., 0.5
cone_pos = (2.9, 0, 2.8)
cone_color = (0.3, 0.6, 0.1, 1.)
cone_specular = (1., 1., 1., 1.)
cone_shininess = 100.

def draw_cone():
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, cone_color)         # отраженный свет
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, cone_specular)     # коэффициент блеска
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, cone_shininess)
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    glutSolidCone(cone_radius, cone_height, polygon_number, polygon_number)
    glPopMatrix()

# матовый цилиндр
cylinder_outer_radius, cylinder_inner_radius = 2, 1
cylinder_pos = (-3, 0, 0)
cylinder_color = (1., 1., 0., 1.)
cylinder_specular = (0., 0., 0., 0.)

def draw_cylinder():
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, cylinder_color)    # отраженный свет
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, cylinder_specular)

    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    glutSolidCylinder(cylinder_inner_radius, cylinder_outer_radius, polygon_number, polygon_number)
    glPopMatrix()    

cylinder_texture = None

cylinder_textured_pos = (3, 0, 0)
# текстурированный цилиндр
def draw_cylinder_textured():
    glEnable(GL_TEXTURE_2D)

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1., 1., 1., 1.))
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)

    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    gluCylinder(qobj, cylinder_inner_radius, cylinder_inner_radius, cylinder_outer_radius, polygon_number,polygon_number)
    glTranslatef(0, 0, cylinder_outer_radius)
    gluDisk(qobj, 0, cylinder_inner_radius, polygon_number, 1)
    glPopMatrix()  


    gluDeleteQuadric(qobj)

    glDisable(GL_TEXTURE_2D)


def draw():
    global cylinder_texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # в кадр попадет все, что внутри усеченной пирамиды от 0.5 до 20 по направлению камеры
    gluPerspective(40., 1., 0.5, 20)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*camera.eye_pos, *camera.center_pos, *camera.up_direction)

    glPushMatrix()
    draw_light()
    glPopMatrix()

    if not cylinder_texture:
        cylinder_texture = texture.read_texture('./resources/Brick_Wall_019_basecolor.jpg')

    draw_objects = ((draw_cube, cube_pos),(draw_cone, cone_pos), (draw_cylinder, cylinder_pos), (draw_cylinder_textured, cylinder_textured_pos))

    for draw_func, pos in draw_objects:
        glPushMatrix()
        glTranslatef(*pos)
        draw_func()
        glPopMatrix()
    


    glFlush()