"""
Write a python program to get the smallest number from a list.
item = [51,7,3,10,8]
"""

item = [51, 7, 3, 10, 8]

min_value = item[0]

for i in item:
    if i < min_value:
        min_value = i
print(min_value)

# Approach -2

item1 = [2, 3, 4, 5, 6]
print(item1)
item1.sort()
print(item1)

print("minmum value :-", item1[0])
