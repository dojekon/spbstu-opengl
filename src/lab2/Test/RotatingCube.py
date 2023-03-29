import sys
from math import cos, sin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0.0
light_pos = [5.0, 5.0, 5.0, 1.0]

def draw_cube():
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.2, 0.2, 0.4, 0.9))
    glutSolidCube(2)

def draw_light():
    # Set the position and color of the light
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    
    # Draw a small sphere to represent the light
    glPushMatrix()
    glTranslatef(light_pos[0], light_pos[1], light_pos[2])
    glutSolidSphere(0.1, 10, 10)
    glPopMatrix()

def draw():
    global angle, light_pos
    
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Set the camera position and orientation
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5.0, 5.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    
    # Set the position and orientation of the cube
    glPushMatrix()
    glRotatef(angle, 0.0, 1.0, 0.0)
    draw_cube()
    glPopMatrix()
    
    # Set the position and orientation of the light
    glPushMatrix()
    glRotatef(angle, 1.0, 0.0, 0.0)
    light_pos[0] = 5.0 * cos(angle / 180.0 * 3.14159)
    light_pos[2] = 5.0 * sin(angle / 180.0 * 3.14159)
    draw_light()
    glPopMatrix()
    
    # Swap the front and back buffers to display the scene
    glutSwapBuffers()
    
    # Update the angle for the next frame
    angle += 1.0

def init():
    # Set the clear color and depth buffer
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    
    # Enable depth testing and lighting
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    # Set the projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 1.0, 0.1, 100.0)
    
def main():
    # Initialize GLUT and create the window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
   # Create the window and set the title
    glutCreateWindow("Red Transparent Cube with Rotating Light")

    # Set the display function and timer function
    glutDisplayFunc(draw)
    glutTimerFunc(10, update, 0)

    # Initialize the scene
    init()

    # Start the main loop
    glutMainLoop()


def update(value):
    # Redraw the scene and set the timer function again
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)

main()