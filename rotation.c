#include <GL/glut.h>

// Polygon vertices
GLfloat polygon[][2] = {
    {100, 200},
    {100, 100},
    {300, 100},
    {200, 0}
};
int num_vertices = 4;


int diagonal_start = 2;
int diagonal_end = 0;

int width = 400;
int height = 300;

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    // Polygon outline (black)
    glColor3f(0.0f, 0.0f, 0.0f);
    glLineWidth(2.0f);
    glBegin(GL_LINE_LOOP);
    for (int i = 0; i < num_vertices; i++) {
        glVertex2f(polygon[i][0], polygon[i][1]);
    }
    glEnd();

    // Splitting diagonal
    glColor3f(1.0f, 0.0f, 0.0f);
    glEnable(GL_LINE_STIPPLE);
    glLineStipple(1, 0x00FF);
    glBegin(GL_LINES);
    glVertex2f(polygon[diagonal_start][0], polygon[diagonal_start][1]);
    glVertex2f(polygon[diagonal_end][0], polygon[diagonal_end][1]);
    glEnd();
    glDisable(GL_LINE_STIPPLE);

    // Vertices
    glColor3f(0.0f, 0.0f, 1.0f);
    glPointSize(6.0f);
    glBegin(GL_POINTS);
    for (int i = 0; i < num_vertices; i++) {
        glVertex2f(polygon[i][0], polygon[i][1]);
    }
    glEnd();

    glutSwapBuffers();
}

void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, width, 0, height);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(width, height);
    glutCreateWindow("After rotation and splitting");

    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMainLoop();

    return 0;
}
