# Write a python program to find the longest words.

path = "E:/Backend/modul 4 assingment/task.txt"

f = open(path,'r')
s = f.read()

lst = s.split()

print(s)
print("\nLongest Word in a File is :",max(lst,key=len))
