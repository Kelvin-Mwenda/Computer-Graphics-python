#include <GL/glut.h>
#include <string.h>

// lighting and materials
void init_lighting() {
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_DEPTH_TEST);
    glShadeModel(GL_SMOOTH);  // Gouraud shading

    // Light properties
    GLfloat light_pos[] = {1.0, 1.0, 2.0, 0.0};
    GLfloat ambient[]   = {0.3, 0.3, 0.3, 1.0};
    GLfloat diffuse[]   = {0.7, 0.7, 0.7, 1.0};
    GLfloat specular[]  = {1.0, 1.0, 1.0, 1.0};

    glLightfv(GL_LIGHT0, GL_POSITION, light_pos);
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse);
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular);

    // Material properties
    GLfloat mat_ambient[]  = {0.2, 0.2, 0.2, 1.0};
    GLfloat mat_diffuse[]  = {0.1, 0.6, 0.9, 1.0};  // Bluish tone
    GLfloat mat_specular[] = {1.0, 1.0, 1.0, 1.0};
    GLfloat shininess      = 50.0;

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
    glMaterialf(GL_FRONT, GL_SHININESS, shininess);
}

//X, Y, Z axes
void draw_labels() {
    void render_text(float x, float y, float z, const char* label) {
        glRasterPos3f(x, y, z);
        for (int i = 0; i < strlen(label); i++) {
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, label[i]);
        }
    }

    glColor3f(0.0, 0.0, 0.0);  // Black labels
    render_text(2.1, 0, 0, "X");
    render_text(0, 2.1, 0, "Y");
    render_text(0, 0, 2.1, "Z");
    render_text(0, 0, 0, "O");
}

void draw_axes() {
    glDisable(GL_LIGHTING);
    glLineWidth(2.0);
    glBegin(GL_LINES);
        // X axis
        glColor3f(1, 0, 0);
        glVertex3f(0, 0, 0);
        glVertex3f(2, 0, 0);

        // Y axis
        glColor3f(0, 1, 0);
        glVertex3f(0, 0, 0);
        glVertex3f(0, 2, 0);

        // Z axis
        glColor3f(0, 0, 1);
        glVertex3f(0, 0, 0);
        glVertex3f(0, 0, 2);
    glEnd();

    draw_labels();
    glEnable(GL_LIGHTING);  // Re-enable lighting
}

// Display callback
void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    gluLookAt(3, 3, 4,  0, 0, 0,  0, 1, 0);  // Camera

    draw_axes();

    // teapot
    glColor3f(0.1, 0.6, 0.9);
    glutSolidTeapot(1.0);

    glutSwapBuffers();
}

// Reshape callback
void reshape(int width, int height) {
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, (float)width / (float)height, 1.0, 20.0);
    glMatrixMode(GL_MODELVIEW);
}

// Main
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(700, 700);
    glutCreateWindow("Gouraud Shading Model - C OpenGL");

    glClearColor(1.0, 1.0, 1.0, 1.0);  // White bg

    init_lighting();

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMainLoop();

    return 0;
}
