# Write a Python program to read last n lines of a file.

path = "E:/Backend/modul 4 assingment/task.txt"

N = int(input("Enter N value : "))

with open(path, 'r') as file:
    data= file.readlines()

print(f"The following are the last {N} lines of a text file :")

for i in (data[-N:]):
    print(i, end ='')
