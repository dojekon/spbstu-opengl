import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math

# Функция для создания текстуры
def load_texture(texture_file):
    texture = pygame.image.load(texture_file)
    texture_data = pygame.image.tostring(texture, "RGBA", 1)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texture.get_width(), texture.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    glBindTexture(GL_TEXTURE_2D, 0)
    return texture_id

# Инициализация
pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Загрузка текстуры
texture_id = load_texture("bricks.jpg")

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    glutInit(sys.argv)

    glRotatef(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Куб с прозрачностью
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(1, 1, 1, 0.7)  # Прозрачность задается здесь
    glutSolidCube(1.0)
    glDisable(GL_BLEND)

    # Конус с полированной поверхностью
    glPushMatrix()
    glTranslatef(2, 0, 0)
    glColor3f(1, 0, 0)
    glMaterialf(GL_FRONT, GL_SHININESS, 128)  # Максимальное значение свойства shininess
    glutSolidCone(0.5, 1, 32, 32)
    glMaterialf(GL_FRONT, GL_SHININESS, 0)
    glPopMatrix()

    # Матовый цилиндр
    glPushMatrix()
    glTranslatef(-2, 0, 0)
    glColor3f(0, 1, 0)
    glMaterialf(GL_FRONT, GL_SHININESS, 0)
    cylinder = gluNewQuadric()
    gluCylinder(cylinder, 0.5, 0.5, 1, 32, 32)
    glPopMatrix()

    # Цилиндр с текстурой (без bump mapping)
    glPushMatrix()
    glTranslatef(0, 2, 0)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glColor3f(1, 1, 1)
    textured_cylinder = gluNewQuadric()
    gluQuadricTexture(textured_cylinder, GL_TRUE)
    gluCylinder(cylinder, 0.5, 0.5, 1, 32, 32)
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

    # Источник света
    glPushMatrix()
    glTranslatef(0, -2, 0)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (-1, 1, 1, 0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1))
    glPopMatrix()

    # Обновление экрана
    pygame.display.flip()
    pygame.time.wait(10)
