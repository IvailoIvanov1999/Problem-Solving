class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, n):
        self.radius = n

    def get_area(self):
        a = self.pi * self.radius ** 2
        return a

    def get_circumference(self):
        return 2 * self.pi * self.radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
