# Write a Python program to copy the contents of a file to another file.



m_file = "E:/Backend/modul 4 assingment/task.txt"

c_file = "E:/Backend/modul 4 assingment/task3.txt"


with open(m_file,'r') as f1:
    read=f1.read()

with open(c_file,'w') as f2:
    f2.write(read)

with open(c_file,'r') as f3:
    c=f3.read()
    
print(c)
