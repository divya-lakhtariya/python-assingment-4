 # Write a Python program to read an entire text file.

path = 'E:/Backend/modul 4 assingment/task.txt'

file = open(path, 'r')

read = file.read()

file.close()

print(read)
