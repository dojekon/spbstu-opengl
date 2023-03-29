import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

verticies_cube = (
    ( 1, -1, -1),
    ( 1,  1, -1),
    (-1,  1, -1),
    (-1, -1, -1),
    ( 1, -1,  1),
    ( 1,  1,  1),
    (-1, -1,  1),
    (-1,  1,  1)
)

edges_cube = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

def Cube():
    glBegin(GL_LINES)
    for edge in edges_cube:
        for vertex in edge:
            glVertex3fv(verticies_cube[vertex])
    glEnd()

def Cone(radius=1, height=1, num_points=16):
    verticies_cone = []
    for i in range(num_points):
        x = radius * math.cos(2*math.pi*i/num_points)
        y = radius * math.sin(2*math.pi*i/num_points)
        verticies_cone.append((x,y,0))
    verticies_cone.append((0,0,height))
    glBegin(GL_LINE_LOOP)
    for i in range(num_points):
        glVertex3fv(verticies_cone[i])
        glVertex3fv(verticies_cone[(i+1)%num_points])
    glEnd()
    glBegin(GL_LINES)
    for i in range(num_points):
        glVertex3fv(verticies_cone[i])
        glVertex3fv(verticies_cone[-1])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(90, (display[0]/display[1]), 0, 50.0)
    glTranslatef(0.0,0.0,-5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 0, 1, 0)
        #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # отрисовываем куб
        glPushMatrix()
        glRotatef(-90, 1, 0, 0)
        glRotatef(45, 0, 1, 0);
        #glScalef(3.0, 3.0, 3.0) # Масштабирование куба с коэф 3
        Cube()
        glPopMatrix()

        
        glPushMatrix()
        glRotatef(-90, 1, 0, 0)
        glRotatef(45, 0, 1, 0)
        glTranslatef(0.0,0.0,1.0)
        Cone(radius=1, height=2, num_points=16)
        glPopMatrix()
            
        pygame.display.flip()
        pygame.time.wait(10)

main()