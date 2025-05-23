# Computer Graphics Project

## Project Overview
This project is focused on implementing various computer graphics techniques using OpenGL. It includes several programs that demonstrate different shading models and rendering techniques. The project is structured to facilitate easy navigation and understanding of the various components involved in computer graphics programming.


## Project Structure
```bash

    ├── .vscode/ # Visual Studio Code configuration files
    │ ├── c_cpp_properties.json # C/C++ properties for IntelliSense
    │ ├── launch.json # Debugging configurations
    │ ├── settings.json # Workspace settings for VSCode
    │ └── tasks.json # Task configurations for building and running
    ├── include/ # Header files for OpenGL and other libraries
    │ ├── GL/ # OpenGL header files
    │ │ ├── freeglut_ext.h
    │ │ ├── freeglut_std.h
    │ │ ├── freeglut.h
    │ │ └── glut.h
    │ ├── glad/ # GLAD header files
    │ │ └── glad.h
    │ ├── GLFW/ # GLFW header files
    │ │ ├── glfw3.h
    │ │ └── glfw3native.h
    │ └── KHR/ # Khronos Group header files
    │ └── khrplatform.h
    ├── lib/ # Library files for linking
    │ ├── freeglut.lib # FreeGLUT library
    │ ├── glfw3.dll # GLFW dynamic link library
    │ ├── libfreeglut_static.a # Static library for FreeGLUT
    │ ├── libfreeglut.a # Static library for FreeGLUT
    │ └── libglfw3dll.a # Static library for GLFW
    ├── myvenv/ # Python virtual environment
    │ ├── include/ # Include files for the virtual environment
    │ ├── Scripts/ # Scripts for the virtual environment
    │ ├── .gitignore # Git ignore file for the virtual environment
    │ └── pyvenv.cfg # Configuration file for the virtual environment
    ├── src/ # Source files for the programs
    │ ├── glad.c # OpenGL loader implementation
    │ ├── stb_easy_font.h # Font rendering library
    │ ├── concave_polygon.c # Concave polygon rendering implementation
    │ ├── Faceted.c # Faceted shading implementation
    │ ├── Faceted.py # Python implementation for faceted shading
    │ ├── Faceted.exe # Compiled executable for faceted shading
    │ ├── Gaurand.c # Gaurand shading implementation
    │ ├── Gouraud.c # Gouraud shading implementation
    │ ├── Gouraud.py # Python implementation for Gouraud shading
    │ ├── Gouraud.exe # Compiled executable for Gouraud shading
    │ ├── Phong.c # Phong shading implementation
    │ ├── Phong.py # Python implementation for Phong shading
    │ ├── Phong.exe # Compiled executable for Phong shading
    │ ├── Rotation.c # Rotation transformations implementation
    │ ├── Rotation.exe # Compiled executable for rotation transformations
    │ ├── Rotational.c # Rotational transformations implementation
    │ ├── Rotational.py # Python implementation for rotational transformations
    │ ├── freeglut.dll # FreeGLUT dynamic link library
    │ └── glfw3.dll # GLFW dynamic link library
    ├── README.md # Project documentation
    └── LICENSE # License file for the project
```


## Program Descriptions
- **Faceted.c**: Implements faceted shading, which gives a polygonal appearance to 3D models.
- **Gouraud.c**: Demonstrates Gouraud shading, which interpolates vertex colors across the surface of polygons.
- **PhongShading.c**: Implements Phong shading, providing a more realistic lighting model by interpolating normals.
- **Rotational.c**: Shows how to apply rotational transformations to objects in a 3D space.
- **concave.c**: Renders a concave polygon and demonstrates basic OpenGL rendering techniques.


## Running the Programs
To run the programs, ensure you have the necessary libraries installed (GLFW, OpenGL, etc.). Follow these steps:

1. **Compile the Programs**:
   Use the following command to compile a specific program (replace `program.c` with the desired file):
   ```bash
   gcc -o program program.c -I"path_to_glfw_include" -L"path_to_glfw_lib" -lglfw -lopengl32 -lgdi32 -luser32
   ```

2. **Run the Compiled Executable**:
   After compiling, run the program with:
   ```bash
      .\program.exe
   ```
   Or just run the 
    ```bash
      .\...exe
    ```
    for example;
    ```bash
      .\Phong.exe
    ```
    files that you see.


## Contributing to the Project
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. **Fork the Repository**: Click on the "Fork" button on the top right of the repository page.

2. **Clone Your Fork**: Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/Kelvin-Mwenda/Computer-Graphics-python.git
   ```

3. **Create a New Branch**: Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**: Implement your changes and test them thoroughly.

5. **Commit Your Changes**: Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add your message here"
   ```

6. **Push to Your Fork**: Push your changes to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**: Go to the original repository and create a pull request from your branch.

Thank you for your interest in contributing to this project!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
