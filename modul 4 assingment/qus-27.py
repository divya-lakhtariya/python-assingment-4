'''
Que-27 : What is used to check whether an object o is an instance of class A?
ans :- In Python, you can use the isinstance() function to check whether an object is an instance of a particular class. The isinstance() function returns True if the object is an instance of the specified class or a tuple of classes, and False otherwise.
'''
Example:--
	class A:
    		pass	
	obj = A()
	result = isinstance(obj, A)
	print(result)
