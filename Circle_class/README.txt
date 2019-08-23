For this assignment, you will make a "Circle" class, which makes use
of your Point class from the previous assignment. Start by creating a
symlink to point.py in the current directory:

  ln -s ../12_point/point.py .

Now in circle.py, you can do:

  from point import Point

and use your Point class there.

For the Circle class:
  - A Docstring summarizing the class.
  - __init__, which takes a Point c and a floating point number r and
    assigns the center and radius respectively. The default values
    should be a point at (0, 0) and radius 1. You should assert that
    the radius is greater than or equal to 0.
  - __str__, which returns a string representation of the circle. For
    example, a circle at (0, 0) with radius 1 would be:
      ((0, 0), 1)
  - __repr__, which returns a more detailed string representation of
    the circle. For example, a circle at (0,0) with radius 1 would be:
      Circle((0, 0), 1)
  - move, which takes dx and dy and moves the center of the circle
    accordingly. Remember, you already wrote move for Point.
  - intersection_area, which takes a parameter other_circle and
    calculates the intersection of self, and other_circle. You will
    likely need a source of domain knowledge for this problem. Also,
    be careful of corner cases--some circles do not intersect, and
    some are entirely inside of another.

Test your code thoroughly! For intersection_area, test simple cases,
as well as more complex ones that you can theoretically verify are
correct. 

You will turn in circle.py for this assignment.
