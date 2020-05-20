person = {"name": "John", "last_name": "Doe", "age": 55}
print(person['name'])
print(person.get('name', 'Empty'))
print(person.get('nickname', 'Empty'))

print('name' in person)

print(person.keys())

print(person.values())

print(person.items())

for k in person.keys():
    print(k)

for v in person.values():
    print(v)

for k, v in person.items():
    print(k, v)

print(person.pop('name', 'Empty'))
print(person)
print(person.pop('nickname', 'Empty'))
print(person)

person.clear()