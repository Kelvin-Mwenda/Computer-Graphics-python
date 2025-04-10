from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)  # <<< GOURAUD SHADING

    # Light properties
    glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 2.0, 0.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    # Material properties
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.1, 0.6, 0.9, 1.0])  # Blueish tone
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 50)


def draw_axes():
    glDisable(GL_LIGHTING)
    glLineWidth(2.0)
    glBegin(GL_LINES)

    # X axis - Red
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(2, 0, 0)

    # Y axis - Green
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 2, 0)

    # Z axis - Blue
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 2)

    glEnd()
    draw_labels()
    glEnable(GL_LIGHTING)


def draw_labels():
    def text(x, y, z, label):
        glRasterPos3f(x, y, z)
        for ch in label:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

    glColor3f(0, 0, 0)  # Black labels
    text(2.1, 0, 0, "X")
    text(0, 2.1, 0, "Y")
    text(0, 0, 2.1, "Z")
    text(0, 0, 0, "O")


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(3, 3, 4, 0, 0, 0, 0, 1, 0)

    draw_axes()

    glColor3f(0.1, 0.6, 0.9)
    glutSolidTeapot(1.0)

    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, width / float(height), 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"Gouraud Shading Model - PyOpenGL")

    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background

    init_lighting()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()
