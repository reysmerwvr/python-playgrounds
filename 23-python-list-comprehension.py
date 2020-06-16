list1 = []
for char in 'home':
    list1.append(char)

print(list1)

# With List Comprehension
list1 = [char for char in 'home']
print(list1)
#######################################################################################################################
list1 = []
for number in range(0, 11):
    list1.append(number ** 2)

print(list1)
# With List Comprehension
list1 = [number**2 for number in range(0, 11)]
print(list1)
#######################################################################################################################
list1 = []
for number in range(0, 11):
    if number % 2 == 0:
        list1.append(number)
print(list1)
# With List Comprehension
list1 = [number for number in range(0, 11) if number % 2 == 0]
print(list1)
#######################################################################################################################
list1 = []
for number in range(0, 11):
    list1.append(number**2)
even = []
for number in list1:
    if number % 2 == 0:
        even.append(number)
print(even)
# With List Comprehension
even = [number for number in [number**2 for number in range(0, 11)] if number % 2 == 0]
print(even)
#######################################################################################################################
