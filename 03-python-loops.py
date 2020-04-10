print(sum(range(0, 101, 2)))
num = 0
add = 0
while num <= 100:
    if num % 2 == 0:
        add += num
    num += 1
print(add)

totalOfNums = int(input("How many numbers do you want to input?: "))
add = 0
for r in range(totalOfNums):
    add += float(input("Type a number: "))
print("Total of numbers: ", totalOfNums, "Addition of those numbers: ", add, "Average :", add / totalOfNums)

numbers = [1, 3, 6, 9]
while True:
    number = int(input("Type a number between 0 and 9: "))
    if 0 <= number <= 9:
        break
if number in numbers:
    print("The number", number, "is in the list", numbers)
else:
    print("The number", number, "is not in the list", numbers)

print(list(range(0, 11)))
print(list(range(-10, 1)))
print(list(range(0, 21, 2)))
print(list(range(-19, 0, 2)))
print(list(range(0, 51, 5)))

list1 = ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
list2 = ["h", "e", "l", "l", "o", " ", "m", "o", "o", "n"]
list3 = []

for char in list1:
    if char in list2 and char not in list3:
        list3.append(char)
print(list3)
