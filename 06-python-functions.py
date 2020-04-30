def greeting():
  print("Hello World")
greeting()

def drawFiveTable():
  for i in range(10):
    print("5 *", i, "=", i * 5)
drawFiveTable()

def test():
  print(l)
# test() Error
l = 10
test()

def test():
  o = 5
  print(o)
test()
o = 10
test()
print(o)

def test():
  return "A string returned"
test()

def test():
  return "A string returned", 20, [1, 2, 3]
c, n, l = test()
print(c, n, l)

def sum(a, b):
  return a + b

result = sum(5, 10)
print(result)

def diff(a, b):
  return a - b
print(diff(1, 2))
print(diff(b=2, a=1))

def diff(a=None, b=None):
  if a == None or b == None:
    print("Error worng parameters")
    return
  return a - b
print(diff())
print(diff(2, 2))

def doubleValue(number):
  number *= 2
n = 10
doubleValue(n)
print(n)

def doubleValues(numbers):
  for i, n in enumerate(numbers):
    numbers[i] *= 2
ns = [10, 50, 100]
doubleValues(ns[:])
print(ns)

def indetPosition(*args):
  for arg in args:
    print(arg)
indetPosition(1, "Hello", [1, 2, 3])


def indetName(**kwargs):
  for kwarg in kwargs:
    print(kwargs[kwarg])
indetName(n=1, s="Hello", l=[1, 2, 3])

def superFunction(*args, **kwargs):
  total = 0
  for arg in args:
    total += arg
  print("Total: ", total)
  for kwarg in kwargs:
    print(kwargs[kwarg])
superFunction(10, 50, -1, 1.56, name="RV", age=28)

def inverseCount(num):
  num -= 1
  if num > 0:
    print(num)
    inverseCount(num)
  else:
    print("Boooom!")
  print("Number", num)
inverseCount(5)


def factorial(num):
  print("Initial Value", num)
  if num > 1:
    num = num * factorial(num - 1)
  print("Final Value ->", num)
  return num
factorial(5)

n = int("10")
f = float("10.5")
s = "A text and a number " + str(10) + " " + str(3.14)
bin(10)
hex(10)
int('0xa', 16)
abs(6)
round(5.5)
round(5.4)
eval('2+5')
n = 10
eval('n*10 - 5')
len("Hello")
len([])
help()

