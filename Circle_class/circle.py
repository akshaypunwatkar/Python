from point import Point
from math import pi, sqrt, acos, hypot

class Circle():
    
    def __init__(self, point = Point(0,0), r = 1):
        if(r <= 0):
            return
        else:
            self.pt = point
            self.rad = r


    def __str__(self):
        return '(' + str(self.pt) + ', ' + str(self.rad) + ')'

    def __repr__(self):
        return 'Circle('+ str(self.pt) +', ' + str(self.rad) + ')'

    def move(self, dx, dy):
        self.pt.move(dx, dy)

    def intersection_area(self, other_circle):
        d= self.pt.distance_from(other_circle.pt)

        dist = hypot(other_circle.pt.x - self.pt.x, other_circle.pt.y - self.pt.y)

        rad0 = self.rad
        rad1 = other_circle.rad
        rr0 = rad0*rad0
        rr1 = rad1*rad1

        if (rad0 == rad1 and self.pt.x == other_circle.pt.x and self.pt.y == other_circle.pt.y):
            return pi*rr0


        if (d >= rad1 + rad0):
            return 0
        elif(d <= abs(rad0 - rad1) and rad0 >= rad1):
            return pi*rr1
        elif(d <= abs(rad0 - rad1) and rad0 < rad1):
            return pi*rr0
        else:
            
            t1 = rr0*acos((d*d + rr0 - rr1)/(2*d*rad0)) 
            t2 = rr1*acos((d*d + rr1 - rr0)/(2*d*rad1)) 
            t3 = (0.5*sqrt((-d+rad0+rad1)*(d+rad0-rad1)*(d-rad0+rad1)*(d+rad0+rad1)))
            area = t1 + t2 - t3
        return area

#def main():
    
#    c1= Circle(Point(-4,-2),4)
#    c2 = Circle(Point(-3,-4),6)
#    print(c1.intersection_area(c2))

#main()    
