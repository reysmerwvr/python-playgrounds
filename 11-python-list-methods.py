list1 = [1, 2, 3, 4, 5, 6]
list1.append(7)
print(list1)

list1.clear()
print(list1)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

["Hello", "World", "World"].count("Hello")
["Hello", "World", "World"].index("Hello")
["Hello", "World", "World"].index("World")

list1 = [1, 2, 3, 4, 5]
list1.insert(0, 0)
print(list1)

list1 = [5, 10, 15, 25]
list1.insert(-1, 20)
print(list1)

list1 = [5, 10, 15, 25]
list1.insert(500, 30)
print(list1)

list1 = [5, 10, 15, 25]
last_number = list1.pop()
print(last_number)
print(list1)

list1 = [5, 10, 15, 25]
list1.remove(25)
print(list1)

list1 = [5, 10, 15, 25, 25]
list1.remove(25)
print(list1)

list1 = [5, 10, 15, 25, 25]
list1.reverse()
print(list1)

list1 = ["Hello", "World"]
list1.reverse()
print(list1)

list1 = "Hello World".split()
list1.reverse()
print(list1)

list1 = list("Hello World")
print(list1)
list1.reverse()
print(list1)
reversed_string = "".join(list1)
print(reversed_string)

list1 = [5, -10, 35, 0, -65, 100]
list1.sort()
print(list1)

list1 = [5, -10, 35, 0, -65, 100]
list1.sort(reverse=True)
print(list1)
