For this assignment, you will write (in point.py) a class "Point,"
which represents the x- and y-position of a point in the Cartesian
plane. As such, it should have fields for x and y.

If you need help, the Python documentation is useful: 
  https://docs.python.org/3/tutorial/classes.html
especially section 9.3.

The Point class should have the following attributes and methods:
  - A docstring summarizing the class.
  - __init__, which takes parameters x and y and default initializes x
    and y to 0.
  - __str__ and __repr__, which give the string and representation of
    a Point object, e.g. for a Point with (1, -2), str would be 
    '(1, -2)', and repr would be 'Point(1, -2)'.
  - move, which takes parameters dx and dy and moves the x and y
    values of the point by those amounts.
  - distance_from, which takes a parameter pt and calculates its
    distance from the current point. Note: there are a variety of
    functions you might find useful in the math module.

Note: If you want to make a copy of a point, you cannot use simple
assignment because that will only copy the underlying pointer, so both
variable names will refer to the same object. You can use the copy
module for copying: 
  https://docs.python.org/3/library/copy.html
or you can pass the object's fields to the constructor you wrote:
  p1copy = Point(p1.x, p1.y)

Make sure you test your code! Test every method, and print often!

For this assignment, you will be turning in point.py.
