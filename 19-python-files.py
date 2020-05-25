from io import open

text = "First line \nSecond line"
file = open('file_test.txt', 'w')
file.write(text)
file.close()
del file

file = open('file_test.txt', 'r')
text = file.read()
file.close()
print(text)
del file

file = open('file_test.txt', 'r')
lines = file.readlines()
file.close()
del file
print(lines)
print(lines[0])
print(lines[-1])

file = open('file_test.txt', 'a')
file.write('\nFour line')
file.close()
del file

file = open('file_test.txt', 'r')
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)
file.close()
del file

with open('file_test.txt', 'r') as file:
    for line in file:
        print(line)

file = open('file_test.txt', 'r')
file.seek(10)
file.read()
file.read()
file.seek(0)
file.read()
file.seek(0)
file.read(5)
file.close()
del file

file = open('file_test.txt', 'r')
file.seek(0)
text = file.read()
file.seek(len(text)/2)
file.read()
file.close()
del file

file = open('file_test.txt', 'r+')
file.write('New Line\n')
file.close()
del file
