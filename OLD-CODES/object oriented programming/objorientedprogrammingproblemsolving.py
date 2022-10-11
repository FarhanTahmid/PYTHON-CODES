#SOLVING PROBLEMS   * FINDING THE VALUE OF DISTANCE AND SLOPE BETWEEN TWO POINTS IN GRAAPH

class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return (y2-y1) / (x2-x1)

c1 = (3,2)
c2 = (8,10)
myline = Line(c1,c2)
myline.distance()
#output: 9.43......
myline.slope()
#output: 1.6


# VOLUME AND SURFACE OF A CYLINDER

class Cylinder:
    def __init__(self,height=1,radius=1):

        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * (self.radius)**2

    def surface_area(self):

        top = 3.14 * (self.radius**2)
        return (2*top) + (2*3.14*self.radius*self.height)

mycyl = Cylinder(2,3)
mycyl.volume()
#output: 56.52...
mycil.surface_area()
#output: 94.2
