import random

# >= 0 and < 1.0
print(random.random())
print(random.random())
# >= 1 and < 10
print(random.uniform(1, 10))
print(random.uniform(1, 10))
# >= 0 and < 10 int
print(random.randrange(1, 10))
print(random.randrange(1, 10))
# >= 0 and < 101 int
print(random.randrange(1, 101))
print(random.randrange(1, 101))
# >= 0 and < 101 int
print(random.randrange(1, 101, 2))
print(random.randrange(1, 101, 5))
word = 'Hello World'
print(random.choice(word))
list_of_numbers = [1, 2, 3]
print(random.choice(list_of_numbers))
random.shuffle(list_of_numbers)
print(list_of_numbers)
print(random.sample(list_of_numbers, 2))
