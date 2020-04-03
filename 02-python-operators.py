n1 = float(input("Type the first number: "))
n2 = float(input("Type the second number: "))
print("Are equals?", n1 == n2)
print("Are different?", n1 != n2)
print("First number is greater than Second number? =", n1 > n2)
print("Second is greater or equal than First number ? =", n2 >= n1)

strTest = input("Type a string: ")
conditions = 3 <= len(strTest) < 10
print("The string is greater or equal than 3 and less than 10? =", conditions)

magicNumber = 12345679
userNumber = int(input("Type a random number between 1 and 9:"))
userNumber *= 9
magicNumber *= userNumber
print("The magic number is: ", magicNumber)
