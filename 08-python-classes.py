import math


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({} {})".format(self.x, self.y)

    def get_quadrant(self):
        if self.x > 0 and self.y > 0:
            print("{} belongs to first quadrant".format(self))
        elif self.x < 0 < self.y:
            print("{} belongs to second quadrant".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} belongs to third quadrant".format(self))
        elif self.x > 0 > self.y:
            print("{} belongs to four quadrant".format(self))
        else:
            print("{} is on the origin".format(self))

    def vector(self, point):
        print("The vector between {} y {} is ({}, {})".format(self, point, point.x - self.x, point.y - self.y))

    def distance(self, point):
        distance = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        print("The distance between the points {} y {} is {}".format(self, point, distance))


class Rectangle:

    def __init__(self, initial_point=Point(), end_point=Point()):
        self.initial_point = initial_point
        self.end_point = end_point
        self.base = 0
        self.height = 0
        self.area = 0

    def get_base(self):
        self.base = abs(self.end_point.x - self.initial_point.x)
        print("The rectangle base is {}".format(self.base))

    def get_height(self):
        self.height = abs(self.end_point.y - self.initial_point.y)
        print("The rectangle height is {}".format(self.height))

    def get_area(self):
        self.base = abs(self.end_point.x - self.initial_point.x)
        self.height = abs(self.end_point.y - self.initial_point.y)
        self.area = self.base * self.height
        print("The rectangle area is {}".format(self.area))


# A(2, 3), B(5, 5), C(-3, -1) y D(0,0)
A = Point(2, 3)
B = Point(5, 5)
C = Point(-3, -1)
D = Point(0, 0)

# A.get_quadrant()
# C.get_quadrant()
# D.get_quadrant()

# A.vector(B)
# B.vector(A)

# A.distance(B)
# B.distance(A)

# A.distance(D)
# B.distance(D)
# C.distance(D)

R = Rectangle(A, B)
R.get_base()
R.get_height()
R.get_area()
