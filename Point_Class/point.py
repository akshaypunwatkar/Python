from math import sqrt
class Point:
    def __init__(self, x1=0,y1=0 ):
        self.x = x1
        self.y = y1

    def __str__(self):
        return ('(' + str(self.x) + ', ' +  str(self.y) +')')
    
    def __repr__(self):
        return 'Point(' + str(self.x)+ ', ' + str(self.y) + ')'

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def distance_from(self,pt):
        return (sqrt(pow(pt.x-self.x,2)+pow(pt.y-self.y,2)))
