# CFD USER-INTERFACE


This provides user interface to CFD softwares Gmesh,Flludity and Paraview which can be used for 

  - Creation of .geo file for pre-procesiing using Gmesh software
  - Creation of .msh file for Solving required situation using Gmesh software
  - Solving Defferntial equation created by gmesh using Fluidity
  - plotting data created by solver
 
this software is build under the course CS 310 Large Application Practicum IIT Mandi
 - #### Course Instructor 
    1. Padmanabhan Rajan
    2. B.D. Chaudhri
 - #### Mentor
    1. Gaurav Bhutani
 - #### TA Mentor
      1.  Jyoti
- #### Group Member
     1. Dinbandhu Kumar Singh
     2. Devesh Soni
     3. Vaibahv Saharan
- #### GitHub Link
     [Unified CFD Software](https://github.com/DinbandhuKumarSingh/Unified-CFD-Software)



# Features!

  - Craete a .geo file
  - Create a new project, select/ create a .geo file click on "Pre-Processing button" for creating mesh
  - Select a .msh select a .fml file click an solver  which will solve differential equation made with the help of .msh and .fml file
  - While opening a existing project if wrong directory selected it will pop-up an error message
  - If a project is already existing in some  directory with same name it won't allow to create.
  - It will keap track of recently worked project and provide a direct link link to that project
  - It will show current status of project through progress-bar
 

## Prereriquisites

This uses a number of open source projects to work properly:

* [GMSH] - used for creating .geo and .msh file!
* [Fludity] - Used for solving mesh
* [Paraview] - Used for interactive, scientific visualization.
* [GCC,GNU Compiler]-The GNU Compiler Collection includes front ends for C, C++.

apart from OSS it usase below python module
* [tkinter]- for creating GUI
* [functool]- gives wrapping to function for interactive use
* [shutil]- provide high level file operation
* [os]-This module provides a portable way of using operating system dependent functionality
* [time]-this provides functions for working with times, and for converting between representations.
* [stat]-The stat module defines constants and functions for interpreting the results of os.stat() , os.fstat() and os.lstat() (if they exist)



### Todos

 - Write MORE Tests
 - Add Night Mode
 - Add Open Foam
 - Add Plot Using Python

License
----

None


**Free Software, Hell Yeah!**

