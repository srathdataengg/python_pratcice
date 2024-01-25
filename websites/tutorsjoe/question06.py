"""
Write a Python program to remove duplicates from a list

Sample Output

[1,2,3,7,2,1,5,6,4,8,5,4]

{1,2,3,4,5,6,7,8}

"""

item = [1, 2, 3, 7, 2, 1, 5, 6, 4, 8, 5, 4]

final = []

for i in item:
    if i not in final:
        final.append(i)

print(final)

# list comprehension approach
res = []

[res.append(i) for i in item if i not in res]

print(res)
