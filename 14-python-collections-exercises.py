quote = "when one door of happiness closes#another opens#but often we look so long at the closed door#that " \
        "we do not see the one which has been opened for us"
# Output:
# When one door of happiness closes...
# - Another opens.
# - But often we look so long at the closed door.
# - That we do not see the one which has been opened for us.
lines = quote.split("#")

for i, line in enumerate(lines):
    lines[i] = line.capitalize()
    startOfLine = "- "
    endOfLine = "."
    if i == 0:
        endOfLine = endOfLine * 3
        lines[i] = lines[i] + endOfLine
    else:
        lines[i] = startOfLine + lines[i] + endOfLine
    print(lines[i])

list1 = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# Delete duplicated elements
# Order list DESC
# Delete odd numbers
# Sum all resulted elements
# Add the Sum value to the first index of the list
# Return the modified list
# Validate the sum list with the following method:
# new_list = modify_list(list_to_modify)
# print( new_list[0] == sum(new_list[1:]) )
# > True


def modify_list(list_to_modify):
    list_to_modify = list(set(list_to_modify))
    list_to_modify.sort(reverse=True)
    for index, number in enumerate(list_to_modify):
        if number % 2 != 0:
            del (list_to_modify[index])
    sum_of_elements = sum(list_to_modify)
    list_to_modify.insert(0, sum_of_elements)
    return list_to_modify


new_list = modify_list(list1)
print(new_list)
print(list1)
print(new_list[0] == sum(new_list[1:]))
