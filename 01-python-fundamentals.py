# What should be printing the next snippet of code?
intNum = 10
negativeNum = -5
testString = "Hello "
testList = [1, 2, 3]

print(intNum * 5)
print(intNum - negativeNum)
print(testString + 'World')
print(testString * 2)
print(testString[-1])
print(testString[1:])
print(testList + testList)

# The sum of each three first numbers of each list should be resulted in the last element of each list
matrix = [
  [1, 1, 1, 3],
  [2, 2, 2, 7],
  [3, 3, 3, 9],
  [4, 4, 4, 13]
]
matrix[1][-1] = sum(matrix[1][:-1])
matrix[-1][-1] = sum(matrix[-1][:-1])
print(matrix)

# Reverse string str[::-1]
testString = "eoD hnoJ,01"
testString = testString[::-1]
print(testString)

n = 0
while n < 10:
    if (n % 2) == 0:
        print(n, 'even number')
    else:
        print(n, 'odd number')
    n = n + 1