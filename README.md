# PROJECT:POLYGON_AREA
## Poject 1: Simple polygon area and perimeter calculater
![Pentagonn](https://user-images.githubusercontent.com/99794453/182675547-2198e4d6-9cdb-429b-b75d-c39671f67166.jpg)
In convex polygon All interior angles are  less than 180 degress. 
In this project our main aim to find the area and perimeter of polygon by that purpose first we declare the vertices 
and second we can declare the each side of the two points. we can find the distnace between the every points automatically we get the length of each side.
By adding all sides lengths we get the perimeter of the polygon 
To find the area first we can divide the polygon into trinagles shape. after we can find the area of all triangles adding all these area to get the Area of polygon
## Project 2: Convex and Concave polygon area and perimeter calculator
![images](https://user-images.githubusercontent.com/99794453/182679801-c11e434d-f2cf-4bd9-bc12-d29a4d4ac927.png)
convex:All interior angles are less than 180 degrees
concave: At least one angle is greater than 180 degrees
complex: set of line segments (sides) connected such that any two segments crossed each other. except edges intersect.
In this project our main aim to find the area and perimeter of polygon by that purpose first we declare the vertices 
and second we can declare the each side of the two points. after declaring the points we can check the shape of the polygon 
because of we can't find the area of the complex polygon area.
first check the it any line segments are intersect to each other or not, if they intersect to each other it is called complex . and also  cross product all points are greater than 0
or all are equl to 0 or all are less than 0 then such type of polygon called convex otherwise it is called concave.
we can find the perimeter by adding all segments lengths
we can find the area of polygon by using shoelace algorithm
## shoelace algorithm
![Screenshot 1](https://user-images.githubusercontent.com/99794453/182764243-f46cdb10-053a-459e-aef1-9381189cdded.png)

The shoelace formula or shoelace algorithm is a mathematical algorithm to determine the area of a simple polygon whose vertices are described by their Cartesian coordinates in the plane.
The method consists of cross-multiplying corresponding coordinates of the different vertices of a polygon to find its area. It is called the shoelace formula because of the constant cross-multiplying for the coordinates making up the polygon, like tying shoelaces. (See table below). This algorithm has applications in 2D and 3D computer graphics graphics, in surveying or in forestry, among other areas.
![Screenshot (69)](https://user-images.githubusercontent.com/99794453/182764281-2b2456b5-e5b2-4091-9a62-3b4faa89214a.png)

To apply the shoelace algorithm you will need to:
List all the vertices in anticlockwise order. (e.g. A,B,C,D,E) in a table, and note the x and y coordinates in two separate columns of the table,
Calculate the sum of multiplying each x coordinate with the y coordinate in the row below (wrapping around back to the first line when you reach the bottom of the table),
Calculate the sum of multiplying each y coordinate with the x coordinate in the row below (wrapping around back to the first line when you reach the bottom of the table),
Subtract the second sum from the first, get the absolute value (Absolute dfference |sum1-sum2|,
Divide the resulting value by 2 to get the actual area of the polygon
![screen](https://user-images.githubusercontent.com/99794453/182765098-1976d57c-e015-4d5b-8932-14f090433d63.png)
