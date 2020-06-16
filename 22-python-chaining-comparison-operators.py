print(1 < 2 < 3) # 1 < 2 and 2 < 3
print(3 > 2 > 1)
print((3 > 2) and (2 > 1))
print((3 > 2) > 1)
print(1 <= True)
# Old way
number = 35

# if number >= 0 and number <= 100:
#     print("The number {} is between 0 and 100".format(number))
# else:
#     print("The number {} is not between 0 and 100".format(number))
# # New way
# number = 35

if 0 <= number <= 100:
    print("The number {} is between 0 and 100".format(number))
else:
    print("The number {} is not between 0 and 100".format(number))