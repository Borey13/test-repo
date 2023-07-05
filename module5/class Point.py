class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def distance_from_zero(self):
        return ((self.x ** 2) + self.y ** 2) ** 0.5

    def distance_from_point(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


p1 = Point(3, 4)
p2 = Point()
p3 = Point(1, 12)
print(p1)
print(p2)
print(p1.distance_from_zero())
print(p1.distance_from_point(p3))
