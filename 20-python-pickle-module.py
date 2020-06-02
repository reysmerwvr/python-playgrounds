import pickle
from io import open
list1 = [1, 2, 3]

file = open('list.pickle', 'wb')

pickle.dump(list1, file)

file.close()

del file

file = open('list.pickle', 'rb')

list1 = pickle.load(file)

print(list1)

del list1

# list1 = pickle.load(file) # Error

file.seek(0)

list1 = pickle.load(file)

print(list1)

file.close()

del file


class Person:

    def __init__(self, first_name):
        self.first_name = first_name

    def __str__(self):
        return self.first_name


names = ["John", "Donald", "Lucy"]

personList = []

for name in names:
    person = Person(name)
    personList.append(person)

print(personList)

file = open('persons.pckl', 'wb')

pickle.dump(personList, file)

file.close()

del file

file = open('persons.pckl', 'rb')

persons = pickle.load(file)

file.close()

for person in persons:
    print(person)
