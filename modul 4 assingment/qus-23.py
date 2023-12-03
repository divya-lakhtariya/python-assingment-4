# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width


rect = rectangle(20,30)
print(rect.area())
