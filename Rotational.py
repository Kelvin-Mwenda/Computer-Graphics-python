import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *  # Import GLUT for text rendering
import numpy as np
import math
import sys

# Define the concave polygon vertices (can modify as needed)
polygon = np.array([[0, 0], [3, 5], [5, 2], [4, -2], [1, -3]])


# Function to plot the polygon
def plot_polygon(polygon, color):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POLYGON)
    for vertex in polygon:
        glVertex2f(vertex[0], vertex[1])
    glEnd()


# Function to rotate the polygon around the origin
def rotate_polygon(polygon, angle):
    rotation_matrix = np.array(
        [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
    )
    return np.dot(polygon, rotation_matrix.T)


# Function to shift polygon to the origin
def shift_to_origin(polygon, vertex_index):
    shifted_polygon = polygon - polygon[vertex_index]
    return shifted_polygon


# Function to check if vertex is below the x-axis
def is_below_x_axis(vertex):
    return vertex[1] < 0


# Function to render text at the specified position
def render_text(text, x, y):
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))


# Rotational splitting function
def rotational_split(polygon):
    split_message = ""
    for i in range(len(polygon)):
        # Shift the polygon so the current vertex is at the origin
        shifted_polygon = shift_to_origin(polygon, i)

        # Rotate the polygon so that the next vertex is on the x-axis
        dx = shifted_polygon[(i + 1) % len(polygon)][0]
        dy = shifted_polygon[(i + 1) % len(polygon)][1]
        angle = np.arctan2(dy, dx)
        rotated_polygon = rotate_polygon(shifted_polygon, -angle)

        # Check if the next vertex is below the x-axis
        if is_below_x_axis(rotated_polygon[2]):
            # Set the split message to show in the GUI
            split_message = f"Polygon split at vertex {i+1}"
            split_polygon1 = rotated_polygon[: i + 2]
            split_polygon2 = rotated_polygon[i + 2 :]
            return split_polygon1.tolist(), split_polygon2.tolist(), split_message

    # If no split needed, return the original polygon and a message indicating no split
    return [rotated_polygon.tolist()], [], "No split required"


# Initialize the GLFW window
if not glfw.init():
    raise Exception("GLFW could not be initialized!")

window = glfw.create_window(800, 800, "Rotational Polygon Split", None, None)

if not window:
    glfw.terminate()
    raise Exception("GLFW window could not be created!")

glfw.make_context_current(window)

# Initialize GLUT (this is required for rendering text)
glutInit(sys.argv)

# Set the projection matrix to be in 2D for our use case
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-5, 5, -5, 5, -1, 1)
glMatrixMode(GL_MODELVIEW)

# Set the background color to white
glClearColor(1.0, 1.0, 1.0, 1.0)  # White background

# Main rendering loop
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)

    # Set up the view (center the view in 2D space)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)

    # Draw the axes (black color)
    glColor3f(0.0, 0.0, 0.0)  # Black for axes
    glBegin(GL_LINES)
    # X axis
    glVertex2f(-5, 0)
    glVertex2f(5, 0)
    # Y axis
    glVertex2f(0, -5)
    glVertex2f(0, 5)
    glEnd()

    # Render axis labels
    render_text("X", 4.5, -0.5)
    render_text("Y", -0.5, 4.5)

    # Perform rotational split and get the split polygons and split message
    split1, split2, split_message = rotational_split(polygon)

    # Draw the original polygon (blue color)
    plot_polygon(polygon, (0.0, 0.0, 1.0))  # Blue for original

    # Check if split1 is not empty
    if len(split1) > 0:
        plot_polygon(np.array(split1), (1.0, 0.0, 0.0))  # Red for first split

    # Check if split2 is not empty
    if len(split2) > 0:
        plot_polygon(np.array(split2), (0.0, 1.0, 0.0))  # Green for second split

    # Render the split message in the window
    render_text(split_message, -4.5, 4.0)

    # Swap buffers to display the scene
    glfw.swap_buffers(window)
    glfw.poll_events()

# Terminate GLFW
glfw.terminate()


# import numpy as np
# import glfw
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *

# # Define the concave polygon vertices
# concave_polygon = [
#     (-0.6, -0.4),
#     (-0.4, 0.6),
#     (0.6, 0.6),
#     (0.4, -0.2),
#     (0.2, -0.6),
#     (-0.6, -0.4),
# ]


# def draw_polygon(vertices, color=(1, 0, 0)):
#     """Draw a polygon with given vertices and color"""
#     glBegin(GL_POLYGON)
#     glColor3fv(color)
#     for vertex in vertices:
#         glVertex2fv(vertex)
#     glEnd()


# def draw_axes():
#     """Draw the x and y axes with labels"""
#     glBegin(GL_LINES)
#     glColor3fv((0, 0, 0))
#     # X axis
#     glVertex2f(-1, 0)
#     glVertex2f(1, 0)
#     # Y axis
#     glVertex2f(0, -1)
#     glVertex2f(0, 1)
#     glEnd()

#     # Draw arrowheads for axes
#     glBegin(GL_LINES)
#     glVertex2f(1, 0)
#     glVertex2f(0.95, 0.05)
#     glVertex2f(1, 0)
#     glVertex2f(0.95, -0.05)

#     glVertex2f(0, 1)
#     glVertex2f(0.05, 0.95)
#     glVertex2f(0, 1)
#     glVertex2f(-0.05, 0.95)
#     glEnd()

#     # Draw axis labels
#     glColor3fv((0, 0, 0))
#     # X axis label
#     render_text("X", 0.98, -0.05)
#     # Y axis label
#     render_text("Y", 0.05, 0.98)


# def render_text(text, x, y):
#     """Helper function to render text at the specified location"""
#     for c in text:
#         glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))


# def split_polygon(vertices):
#     """Splitting the concave polygon using the rotational method"""
#     # Here, you would implement the logic for rotational splitting, for simplicity, just split into two triangles.
#     # This is a simplified approach. In a full implementation, you would calculate intersection points and split.
#     # Return two polygons for demonstration
#     polygon1 = [vertices[0], vertices[1], vertices[2]]
#     polygon2 = [vertices[0], vertices[2], vertices[3], vertices[4], vertices[5]]
#     return polygon1, polygon2


# def setup_viewport():
#     """Set up the OpenGL viewport"""
#     glClearColor(1, 1, 1, 1)  # White background
#     glClear(GL_COLOR_BUFFER_BIT)
#     glLoadIdentity()
#     glOrtho(-1, 1, -1, 1, -1, 1)


# def main():
#     """Main function to create window and draw the scene"""
#     if not glfw.init():
#         return

#     window = glfw.create_window(800, 800, "Concave Polygon Split", None, None)
#     if not window:
#         glfw.terminate()
#         return

#     glfw.make_context_current(window)

#     # Initialize GLUT before using any GLUT functionality
#     glutInit()

#     setup_viewport()

#     while not glfw.window_should_close(window):
#         glClear(GL_COLOR_BUFFER_BIT)

#         draw_axes()

#         # Draw the original concave polygon
#         draw_polygon(concave_polygon, color=(1, 0, 0))

#         # Split the concave polygon into two polygons
#         polygon1, polygon2 = split_polygon(concave_polygon)

#         # Draw the resulting polygons
#         draw_polygon(polygon1, color=(0, 1, 0))
#         draw_polygon(polygon2, color=(0, 0, 1))

#         glfw.swap_buffers(window)
#         glfw.poll_events()

#     glfw.terminate()


# if __name__ == "__main__":
#     main()
