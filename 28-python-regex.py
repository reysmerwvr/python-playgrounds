# https://docs.python.org/3.5/library/re.html#regular-expression-syntax
# https://developers.google.com/edu/python/regular-expressions
# https://www.tutorialspoint.com/python/python_reg_expressions.htm
# http://www.python-course.eu/python3_re.php
# http://www.python-course.eu/python3_re_advanced.php

import re

text = "In this string there is a magic world"

print(re.search('magic', text))

print(re.search('Hello', text))

found = re.search('magic', text)
if found is not None:
    print("The word has been found!")
else:
    print("The word has not been found!")

print(found.start())
print(found.end())
print(found.span())
print(found.string)

#######################################################################################################################

text = "Hello World"

print(re.match('Hello', text))

text = "Hello World"

print(re.match('Ball', text))

#######################################################################################################################

text = "Hello World Hello World"

print(re.split(' ', text))

#######################################################################################################################

text = "Hello World Hello World"

print(re.sub('World', 'Mac', text))

#######################################################################################################################

text = "Hello World Hello World Hello"

print(re.findall('Hello', text))

text = "Hello World Hello World Hello"

print(len((re.findall('Hello', text))))

text = "Hello World Hello World Hello Bye hello"

print(re.findall('Hello|hello', text))

#######################################################################################################################

text = "Helo Hello hello HELLO hllo helo heeelo"

print(re.findall('helLo', text))


def search(patterns, txt):
    for pattern in patterns:
        print(re.findall(pattern, txt))


patterns_list = ['hello', 'helLo', 'HELLO']
search(patterns_list, text)

patterns_list = ['He*', 'He+', 'he?', 'he?llo']
search(patterns_list, text)

patterns_list = ['he{0}llo', 'he{1}llo', 'he{3}lo']
search(patterns_list, text)

patterns_list = ['he{0,1}llo', 'he{1,2}llo', 'he{2,10}lo']
search(patterns_list, text)

#######################################################################################################################

text = "Hallo Hello Hillo Hollo Hullo"
patterns_list = ['H[ae]llo', 'H[aei]llo', 'H[aeiou]llo']
search(patterns_list, text)

#######################################################################################################################
text = "Haallo Heeello Hiiiiillo Hoooollo Huuullo"
patterns_list = ['H[ae]llo', 'H[ae]*llo', 'H[io]{3,9}llo']
search(patterns_list, text)

#######################################################################################################################
text = "Hallo Hello Hillo Hollo Hullo"
patterns_list = ['H[e]llo', 'H[^e]llo']
search(patterns_list, text)

text = "This Python 3 course was released in 2016"
patterns_list = [r'\d', r'\d+', r'\D', r'\D+', r'\s', r'\S', r'\w', r'\w+', r'\W', r'\W+']
search(patterns_list, text)
