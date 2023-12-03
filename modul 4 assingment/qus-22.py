# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

'''
class : class is a blueprint for creating objects.

Self :  It is refers to the instance of the class and
        When you create an instance of the class, it is passed automatically,
        and you can access the instance's attributes and methods using it.
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age

