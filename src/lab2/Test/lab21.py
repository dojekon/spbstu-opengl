import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

# Функция загрузки текстуры
def load_texture(file_name):
    image = Image.open(file_name)
    width, height = image.size
    image_data = image.tobytes("raw", "RGBX", 0, -1)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    return texture_id

# Инициализация GLUT
glutInit()

# Установка режима отображения
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

# Инициализация Pygame и OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

# Установка матрицы проекции
glMatrixMode(GL_PROJECTION)
gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

# Начальная позиция камеры
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0, 0.0, -5.0)

# Создание источника света
light_pos = [2.0, 2.0, 2.0, 1.0]
light_color = [1.0, 1.0, 1.0, 1.0]
light_ambient = [0.2, 0.2, 0.2, 1.0]
glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)
glLightfv(GL_LIGHT0, GL_SPECULAR, light_color)
glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
glEnable(GL_LIGHT0)

# Включение освещения и включение текстур
glEnable(GL_LIGHTING)
glEnable(GL_TEXTURE_2D)

# Создание куба с прозрачностью от 0.5 до 0.9
def create_cube():
    glPushMatrix()
    glTranslatef(-1.5, 2.0, -2.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.2, 0.2, 0.4, 0.7))
    glutSolidCube(2)
    glPopMatrix()


# Создание конуса с максимальным значением shininess
def create_cone():
    glPushMatrix()
    glTranslatef(-3, 0.0, -2.0)
    specular = [1.0, 1.0, 1.0, 1.0]
    shininess = 128
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMateriali(GL_FRONT, GL_SHININESS, shininess)
    glutSolidCone(1.0, 2.0, 32, 32)
    glPopMatrix()

def create_cylinder():
    glPushMatrix()
    glTranslatef(1.5, 0.0, -2.0)
    ambient = [0.5, 0.5, 0.5, 1.0]
    diffuse = [0.5, 0.5, 0.5, 1.0]
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glutSolidCylinder(1.0, 2.0, 32, 32)
    glPopMatrix()

def create_textured_cylinder():
    glPushMatrix()
    glTranslatef(0.0, 0.0, 2.0)
    # Загрузка текстуры и normal map
    texture_id = load_texture("Brick_Wall_019_basecolor.jpg")
    normal_map_id = load_texture("Brick_Wall_019_normal.jpg")
    # Включение и настройка текстурного модулирования
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    # Включение и настройка Bump-mapping
    glActiveTexture(GL_TEXTURE1)
    glBindTexture(GL_TEXTURE_2D, normal_map_id)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_COMBINE)
    glTexEnvi(GL_TEXTURE_ENV, GL_COMBINE_RGB, GL_DOT3_RGB)
    glTexEnvi(GL_TEXTURE_ENV, GL_SOURCE0_RGB, GL_TEXTURE)
    glTexEnvi(GL_TEXTURE_ENV, GL_OPERAND0_RGB, GL_SRC_COLOR)
    glTexEnvi(GL_TEXTURE_ENV, GL_SOURCE1_RGB, GL_TEXTURE1)
    glTexEnvi(GL_TEXTURE_ENV, GL_OPERAND1_RGB, GL_SRC_COLOR)
    # Отрисовка цилиндра
    glColor4f(1.0, 1.0, 1.0, 1.0)
    glutSolidCylinder(1.0, 2.0, 32, 32)
    # Отключение текстур и bump-mapping
    glActiveTexture(GL_TEXTURE0)
    glDisable(GL_TEXTURE_2D)
    glActiveTexture(GL_TEXTURE1)
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

glRotatef(-90, 1, 0, 0)

# Главный цикл приложения
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Изменение параметров источника света
    light_pos[0] = 2.0 * pygame.time.get_ticks() % 1000 / 1000.0
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    
    # Создание объектов
    create_cube()
    create_cone()
    create_cylinder()
    create_textured_cylinder()

    pygame.display.flip()
    pygame.time.wait(10)



