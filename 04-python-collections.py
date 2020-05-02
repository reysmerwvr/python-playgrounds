# Tuples
tuple1 = (100, "Hello", [1, 2, 3], -50)
tuple1[0]
tuple1[-1]
tuple1[2:]
tuple1[2][-1]
print(len(tuple1))
print(len(tuple1[2]))
print(tuple1.index('Hello'))
print(tuple1.count(100))

# Sets
set1 = set()
set2 = {"1", "2", "3"}
set1 = {1, 2, 3}
set1.add(0)
set1.add("H")

# Dictionaries
user = {'name': "John", "last-name": "Doe"}
type(user)
del (user["last-name"])
ages = {"John": 27, "Lisa": 28}
ages["John"] += 1
for name in ages:
    print(name, ages[name])
for name, age in ages.items():
    print(name, age)

# Queues
from collections import deque

queue = deque()
print(queue)
queue = deque(["John", "Lisa", "Me"])
print(queue)
queue.append("Mary")
queue.popleft()
print(queue)
