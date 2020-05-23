from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple

list1 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 3]
print(Counter(list1))

word = 'word'
print(Counter(word))

animals = "cat dog bird dog bird cat"
print(Counter(animals))

counter = Counter(animals.split())
print(counter.most_common(1))
print(counter.most_common(2))
print(counter.most_common())

list1 = [10, 20, 30, 40, 50, 50, 40, 20, 30, 10, 10]
counter = Counter(list1)
print(counter.items())
print(counter.keys())
print(counter.values())
print(sum(counter.values()))
print(list(counter))
dictionary = dict(counter)
print(dictionary)
print(set(counter))

dictionary = defaultdict(int)
print(dictionary['some'])
print(dictionary)

dictionary = defaultdict(str)
print(dictionary['some'])
print(dictionary)

dictionary = defaultdict(object)
print(dictionary['some'])
print(dictionary)

dictionary = defaultdict(int)
dictionary['some'] = 10.5
print(dictionary['something'])
print(dictionary)

dictionary = {'name': 'Jonh', 'last_name': 'Doe'}
print(dictionary)

dictionary = OrderedDict()
dictionary['name'] = 'Jonh'
dictionary['last_name'] = 'Doe'
print(dictionary)

dictionary1 = {'name': 'Jonh', 'last_name': 'Doe'}
print(dictionary1)

dictionary2 = {'last_name': 'Doe', 'name': 'Jonh'}
print(dictionary2)

print(dictionary1 == dictionary2)


tuple1 = (10, 20, 30, 40)
print(tuple1[0])
print(tuple1[-1])

Person = namedtuple('Person', 'name last_name age')
person = Person(name='Jonh', last_name='Doe', age=28)
print(person.name)
print(person.last_name)
print(person.age)
print(person[0])
print(person[1])
print(person[-1])