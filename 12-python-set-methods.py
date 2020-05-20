set1 = set()
set1.add(1)
set1.add(2)
set1.add(3)
print(set1)

set1.discard(1)
print(set1)
set1.add(1)
print(set1)

set2 = set1.copy()
set2.discard(3)
print(set2)
print(set1)

set2.clear()
print(set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {-1, 99}
set4 = {1, 2, 3, 4, 5}
print('---isdisjoint---')
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
print('---issubset---')
print(set1.issubset(set4))
print(set2.issubset(set4))
print(set3.issubset(set4))
print('---issuperset---')
print(set1.issuperset(set4))
print(set2.issuperset(set4))
print(set3.issuperset(set4))
print(set4.issuperset(set1))
print(set4.issuperset(set2))
print(set4.issuperset(set3))

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set4 = {1, 2, 3, 4, 5}
print(set1.union(set2))
print(set1.union(set2) == set4)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {-1, 99}
set4 = {1, 2, 3, 4, 5}
print(set1.difference(set2))
print(set1.difference(set3))
print(set1.difference(set4))

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {-1, 99}
set4 = {1, 2, 3, 4, 5}
print(set1.intersection(set2))
print(set1.intersection(set3))
print(set1.intersection(set4))

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.symmetric_difference(set2))