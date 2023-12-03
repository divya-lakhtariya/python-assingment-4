 # Write a Python program to read a file line by line and store it into a list.

path = "E:/Backend/modul 4 assingment/task.txt"

l = []

with open(path, 'r') as file:
    for i in file:
        l.append(i.strip())

print(l)
