# Write a Python program to write a list to a file.

path = "E:/Backend/modul 4 assingment/task.txt"

l=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

file=open(path,'w')
for i in l:
    file.write(str(i)+'\n')
file.close()

with open(path,'r') as file:
    read=file.read()
print(read)
