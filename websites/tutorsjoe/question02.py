"""
Write a python program to multiply all the items in a list
Ex:- [3,4,5,6,7]
"""

item = [3, 4, 5, 6, 7]
result = 1
for i in item:
    result *= i
print(result)

total = 1
total = [total * i for i in item]
print(total)
