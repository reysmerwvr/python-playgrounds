numbers = range(0, 101)


def multiple(number):
    if number % 5 == 0:
        return True
    return False


print(list(filter(multiple, numbers)))

f = filter(multiple, numbers)

next(f)

print(list(filter(lambda number: number % 5 == 0, numbers)))


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

kids = filter(lambda person: person.age < 18, people)
for kid in kids:
    print(kid)
