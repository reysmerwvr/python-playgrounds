import sys

if len(sys.argv) >= 3:
    text = str(sys.argv[1])
    iterations = int(sys.argv[2])
    for i in range(iterations):
        print(text + str(i))
else:
    print('Error: Missing arguments')

text = "Text 1"
num = int("10")
print("First Text ", text, "a number", num)
stringTest = "First Text '{}' and a number '{}'".format(text, num)
print(stringTest)
print("First Text '{1}' and a number '{0}'".format(text, num))
print("First Text '{t}' and a number '{n}'".format(t=text, n=num))
print("{:>30}".format("string"))  # Alignment to right
print("{:30}".format("string"))  # Alignment to left
print("{:^30}".format("string"))  # Alignment to center
print("{:.3}".format("string"))  # Trunk
print("{:>30.3}".format("string"))  # Alignment to right and Trunked
# Format numbers
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))
# Format numbers with zero
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))
# Format float numbers
print("{:.2f}".format(3.1415926))
print("{:.3f}".format(153.21))
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))
print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))

print("{:>20}".format("Hello World"))
print("{:.3}".format("Hello World"))
print("{:^20.1}".format("Hello World"))
print("{:05d}".format(150))
print("{:7d}".format(7887))
print("{:07.3f}".format(20.02))

if len(sys.argv) >= 3:
    rows = int(sys.argv[1])
    columns = int(sys.argv[2])
    if 9 < rows < 1 and 9 < columns < 1:
        print('Error: Wrong Arguments')
        print('Example: script.py [1-9] [1-9]')
    else:
        for r in range(rows):
            print("")
            for c in range(columns):
                print(" * ", end='')

else:
    print('Error: Missing Arguments')
    print('Example: script.py [1-9] [1-9]')
