# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle


class circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.1416*(self.radius**2)


circle = circle(5)
print(circle.area())
