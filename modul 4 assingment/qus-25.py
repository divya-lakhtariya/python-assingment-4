# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

'''
Inheritance :- Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (subclass or derived class)
 to inherit properties and behaviors (attributes and methods) from another class (superclass or base class).
 This promotes code reusability and allows you to create a hierarchy of classes.

example :-
      class Animal:  
        def speak(self):  
        print("Animal Speaking")  
 
      class Dog(Animal):  
        def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()

init : The __init__ method is a special method in Python classes, also known as the constructor.
       It is automatically called when an object of the class is created.
       The primary purpose of the constructor is to initialize the attributes of the object.
'''
