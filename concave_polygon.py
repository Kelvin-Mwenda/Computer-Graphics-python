from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Polygon vertices
polygon = [(100, 200), (100, 100), (300, 100), (200, 0)]
width, height = 400, 300

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)  # Black outline
    glLineWidth(2)

    #polygon outline
    glBegin(GL_LINE_LOOP)
    for x, y in polygon:
        glVertex2f(x, y)
    glEnd()

    #vertices
    glPointSize(6)
    glBegin(GL_POINTS)
    for x, y in polygon:
        glVertex2f(x, y)
    glEnd()

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Concave Polygon")
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
