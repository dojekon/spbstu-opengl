import sys
import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

rotation = 0.0  # Угол поворота источника света

def init():
    glEnable(GL_LIGHTING)  # Включить освещение
    glEnable(GL_LIGHT0)  # Включить источник света 0
    glEnable(GL_DEPTH_TEST)  # Включить буфер глубины
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Очистить фон черным цветом
    

def draw():
    global rotation
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Очистить буферы
    glLoadIdentity()

    # Переместить и повернуть источник света вокруг объекта
    glPushMatrix()
    glRotatef(rotation, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, -10.0)
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.0, 0.0, 1.0])
    glPopMatrix()

    # рисование куба
    glPushMatrix()
    glRotate(15,1,1,0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.2, 0.2, 0.4, 0.7))
    glutSolidCube(0.5)
    glFlush()
    glPopMatrix()


    glutSwapBuffers()  # Переключить буферы

def update():
    global rotation
    rotation += 1.0  # Увеличить угол поворота
    glutPostRedisplay()  # Запросить перерисовку

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(900, 900)
glutCreateWindow("Python OGL Program")
glutDisplayFunc(draw)
glutIdleFunc(update)
init()
glutMainLoop()
