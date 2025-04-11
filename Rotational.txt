from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Vertex coordinates
polygon = [(100, 200), (100, 100), (300, 100), (200, 0)]
diagonal = (2, 0)

width, height = 400, 300

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # polygon outline
    glColor3f(0.0, 0.0, 0.0)  # Black
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    for x, y in polygon:
        glVertex2f(x, y)
    glEnd()

    # splitting diagonal
    glColor3f(1.0, 0.0, 0.0)  # Red
    glLineStipple(1, 0x00FF)
    glEnable(GL_LINE_STIPPLE)
    glBegin(GL_LINES)
    glVertex2f(*polygon[diagonal[0]])
    glVertex2f(*polygon[diagonal[1]])
    glEnd()
    glDisable(GL_LINE_STIPPLE)

    # vertices
    glColor3f(0.0, 0.0, 1.0)
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
    glutCreateWindow(b"After rotation and splitting")
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
