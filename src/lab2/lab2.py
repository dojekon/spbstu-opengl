import draw as draw
import cameraMotion as camera

from OpenGL.GL import *
from OpenGL.GLUT import *


w, h = 1000, 1000

light_color_delta = 0.05
light_const_attenuation_delta = 0.1
light_pos_delta = 0.1


def handle_char_keys(key, *args):

    if key == b' ':
        draw.light_const_attenuation = light_const_attenuation_delta \
            if draw.light_const_attenuation + light_const_attenuation_delta > 1.5 \
            else draw.light_const_attenuation + light_const_attenuation_delta

    elif key in [b'r', b'g', b'b']:
        if key == b'r':
            draw.light_color[0] = 0 \
                if draw.light_color[0] + light_color_delta > 1 \
                else draw.light_color[0] + light_color_delta
        elif key == b'g':
            draw.light_color[1] = 0 \
                if draw.light_color[1] + light_color_delta > 1 \
                else draw.light_color[1] + light_color_delta
        elif key == b'b':
            draw.light_color[2] = 0 \
                if draw.light_color[2] + light_color_delta > 1 \
                else draw.light_color[2] + light_color_delta

    elif key in [b'w', b'a', b's', b'd']:
        if key == b'w':
            draw.light_pos[1] += light_pos_delta
        elif key == b's':
            draw.light_pos[1] -= light_pos_delta
        elif key == b'd':
            draw.light_pos[0] += light_pos_delta
        elif key == b'a':
            draw.light_pos[0] -= light_pos_delta

    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)

    glutInitWindowSize(w, h)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Lab 2")

    glClearColor(0., 0., 0., 0.)

    glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_ALPHA_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glViewport(0, 0, w, h)

    glutDisplayFunc(draw.draw)
    glutSpecialFunc(camera.handle_special_keys)
    glutKeyboardFunc(handle_char_keys)

    glutMainLoop()


if __name__ == '__main__':
    main()