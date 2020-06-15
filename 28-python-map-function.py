numbers = range(0, 101)


def double(number):
    return number * 2


doubled_iterator = map(double, numbers)
print(next(doubled_iterator))

print(list(doubled_iterator))

print(list(map(lambda x: x * 2, numbers)))

#######################################################################################################################

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print(list(map(lambda x, y: x * y, a, b)))

#######################################################################################################################

c = [11, 12, 13, 14, 15]

print(list(map(lambda x, y, z: x * y * z, a, b, c)))

#######################################################################################################################


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} of {} years".format(self.name, self.age)


people = [
    Person("John", 35),
    Person("Marta", 25),
    Person("Manuel", 12),
    Person("Ruck", 15),
]


def increment_age(human):
    human.age += 1
    return human


people = map(increment_age, people)

for person in people:
    print(person)

people = [
    Person("John", 35),
    Person("Marta", 25),
    Person("Manuel", 12),
    Person("Ruck", 15),
]

people = map(lambda human: Person(human.name, human.age + 1), people)
for person in people:
    print(person)
