from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

    # Set light properties
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 2, 0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1])

    # Set material properties for Phong shading
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 0.5, 0.0, 1])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1])
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
    def draw_text(x, y, z, text):
        glRasterPos3f(x, y, z)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

    glColor3f(0, 0, 0)  # Black labels
    draw_text(2.1, 0, 0, "X")
    draw_text(0, 2.1, 0, "Y")
    draw_text(0, 0, 2.1, "Z")
    draw_text(0, 0, 0, "O")  # Origin


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(3, 3, 4, 0, 0, 0, 0, 1, 0)

    draw_axes()

    glColor3f(1.0, 0.5, 0.0)  # Orange
    glutSolidTeapot(1.0)  # Demonstrating Phong Shading

    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(w) / float(h), 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"Phong Shading - PyOpenGL")

    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background

    init_lighting()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()
