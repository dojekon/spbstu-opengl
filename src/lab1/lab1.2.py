import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Инициализация Pygame и OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Создание перспективной проекции
gluPerspective(100, (display[0]/display[1]), 0.1, 50.0)

# Начальное местоположение камеры
glTranslatef(0.0, 0.0, -5)

# Функция для создания цилиндра
def create_cylinder(radius, height, slices):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, height/2, 0)
    for i in range(slices+1):
        glVertex3f(radius * math.cos(i * 2*math.pi / slices), height/2, radius * math.sin(i * 2*math.pi / slices))
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, -height/2, 0)
    for i in range(slices+1):
        glVertex3f(radius * math.cos(i * 2*math.pi / slices), -height/2, radius * math.sin(i * 2*math.pi / slices))
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)
    for i in range(slices+1):
        glVertex3f(radius * math.cos(i * 2*math.pi / slices), height/2, radius * math.sin(i * 2*math.pi / slices))
        glVertex3f(radius * math.cos(i * 2*math.pi / slices), -height/2, radius * math.sin(i * 2*math.pi / slices))
    glEnd()

# Создание большого цилиндра
glPushMatrix()
glColor3f(1, 0, 0)  # Красный цвет
glTranslatef(0, -1, 0)  # Перемещение вниз на 1 единицу по оси y
create_cylinder(1, 2, 30)  # Радиус, высота, число сегментов
glPopMatrix()

# Создание малого цилиндра с масштабированием
glPushMatrix()
glColor3f(0, 1, 0)  # Зеленый цвет
glTranslatef(0, 0.5*3.75, 0)  # Перемещение вверх на 0.5 единицы по оси y
glScalef(3.75, 3.75, 3.75)  # Масштабирование вдоль оси Y
create_cylinder(0.5, 1, 20)  # Радиус, высота, число сегментов
glPopMatrix()

# Отображение на экране
pygame.display.flip()

# Цикл для отслеживания событий Pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
