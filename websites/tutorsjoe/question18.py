"""
Write a Python program to flatten a shallow list

Sample Output

[[20,30,70],[30,90,10], [30,20], [70,90,10,80]]

[20, 30, 70, 30, 90, 10, 30, 20, 70, 90, 10, 80]
"""

# Approach -1
li = [[20, 30, 70], [30, 90, 10], [30, 20], [70, 90, 10, 80]]
print("original shallow list :-", li)

flatlist = []
for sublist in li:
    for element in sublist:
        flatlist.append(element)

print("flat list is :-", flatlist)

# Approach -2 using a list comprehension

newlist = [element for element in sublist for sublist in li]

print("new flatten list :", newlist)

# using itertools(chain())

import itertools

flatlist1 = list(itertools.chain(*li))
print("flat list :", flatlist1)
