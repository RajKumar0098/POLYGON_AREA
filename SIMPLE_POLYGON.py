# find out the convex polygon area and perimeter
from math import sqrt
class Polygon:
    def __init__(self,*vertices):
        self.vertices=[Polygon.Point(v[0],v[1]) for v in vertices]
    @property 
    def lines(self):  
        allLines=[Polygon.LSeg(self.vertices[i],self.vertices[i+1]) for i in range(len(self)-1)]
        allLines.append(Polygon.LSeg(self.vertices[len(self)-1],self.vertices[0]))
        return allLines
    @property
    def area(self):  # it returns the area of polygon
        total=0
        for i in range(len(self)-2):
            tri=Polygon.Triangle(self.vertices[0],self.vertices[i+1],self.vertices[i+2])
            total+=tri.area
        return total
    @property
    def perimeter(self):  # It returns the perimeter of polygon
        return sum([abs(line) for line in self.lines])
    def __len__(self):    # It returns the length of the vertices
        return len(self.vertices)
    class LSeg:
        def __init__(self,p1,p2):
            self.p1=p1
            self.p2=p2
        def __abs__(self):    # It returns the distance between two pints 
            return self.p1.dist(self.p2)
        def __repr__(self):
            return f'{self.p1}--{self.p2}'
    class Point:
        def __init__(self,x,y):
            self.x=x
            self.y=y
        def dist(self,other):  # distance between two points is ---> sqrt((x2-x1)^2+(y2-y1)^2)
            return sqrt((self.x-other.x)**2+(self.y-other.y)**2)     
        def __repr__(self):
            return f'({self.x},{self.y})'
    class Triangle:
        def __init__(self,p1,p2,p3):
            self.p1=p1
            self.p2=p2
            self.p3=p3
        
        @property
        def area(self):        # AREA OF TRAINGLE WITH COORDINATES IS --->{ 1/2 (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))}
            a=self.p1.x*(self.p2.y-self.p3.y)
            b=self.p2.x*(self.p3.y-self.p1.y)
            c=self.p3.x*(self.p1.y-self.p2.y)
            return abs(a+b+c)/2
poly2=Polygon((5.09,5.80), (7.00,2.83), (4.76,0.10), (1.48,1.38), (1.68,4.90))
print("area of polygon is--->",poly2.area)
print("perimeter of polygon is --->",poly2.perimeter)
