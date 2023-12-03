# Write a Python program to append text to a file and display the text.

path = "E:/Backend/modul 4 assingment/task.txt"

file = open(path, "a")
file.write("\nHello, tops tecnologis!")
file.close()

file = open(path, "r")
content = file.read()

print("File content:")
print(content)

file.close()
