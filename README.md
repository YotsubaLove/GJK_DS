Collision Detection and Minimum Distance Calculation Using the GJK Algorithm
Overview
This repository contains a Python implementation of the Gilbert-Johnson-Keerthi (GJK) algorithm for collision detection and minimum distance calculation between convex shapes, developed as part of my undergraduate thesis. The project aims to apply computational geometry methods to real-time applications, including vehicle-bicycle collision avoidance simulations, visualization, distance calculation, and benchmarking.

File Structure
filetest.py:
A preprocessing module that reads vehicle and bicycle position, radius, and speed data from a CSV file and generates coordinate data.

gjk3.py:
A module containing the GJK algorithm implementation for collision detection between convex polygons, calculation of minimum distances and closest point pairs, and visualization
functions.

oneto4.py:
  A module that calculates and returns the four vertex coordinates of vehicles and bicycles based on the center of gravity coordinates output from a driving simulator, 
  along with the vehicle length, width, and absolute heading angle used in experiments. It generates rectangular models of vehicles and bicycles and uses gjk3.py to compute the 
  minimum distance and perform collision detection at each time step.

Key Features
  ✅ Collision detection between convex shapes using the GJK algorithm
  ✅ Calculation of minimum distances and closest point pairs
  ✅ Vertex coordinate calculation using center of gravity and heading data from a driving simulator
  ✅ Shape generation and movement simulation for vehicles and bicycles
  ✅ Output of vehicle speed upon collision detection
  ✅ Visualization using Matplotlib

Required Libraries
  numpy
  matplotlib
  pandas

Usage Example
python oneto4.py
  Prepare a CSV file (xxx.csv) containing vehicle and bicycle position, speed, and absolute heading angle data.

  When the distance becomes zero, a collision is detected, and the vehicle speed at that time is output.

Future Plans
  1,Extension to 3D space
  2,Application to more complex polygonal and mesh data
  3,Improved visualization tools
