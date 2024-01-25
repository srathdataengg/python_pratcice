"""
Write a python program to get the largest number from list
i/p - [2,3,4,56,76,65] - o/p - 76
"""

item = [2, 3, 4, 56, 76, 65]

# Approach -1

max = item[0]

for i in item:
    if i > max:
        max = i
print(max)

# Time complexity - O(n)

# Approach -2

item1 = [2, 3, 4, 56, 76, 65]
item1 = item1.sort()
print(item[-1])