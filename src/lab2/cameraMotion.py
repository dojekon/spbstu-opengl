from OpenGL.GLUT import *


eye_pos = [5., 2., 5.]
center_pos = (0., 0., 0.)
up_direction = (0., 1., 0.)

delta = 0.1


def handle_special_keys(key, *args):
    global eye_pos

    if key == GLUT_KEY_UP and glutGetModifiers() == 1:
        eye_pos[2] += delta
    elif key == GLUT_KEY_DOWN and glutGetModifiers() == 1:
        eye_pos[2] -= delta

    elif key == GLUT_KEY_RIGHT:
        eye_pos[0] += delta
    elif key == GLUT_KEY_LEFT:
        eye_pos[0] -= delta

    elif key == GLUT_KEY_UP:
        eye_pos[1] += delta
    elif key == GLUT_KEY_DOWN:
        eye_pos[1] -= delta

    glutPostRedisplay()