"""
Write a Program that get two lists as input and check if they have at least one common member

Sample Output

[1,2,3,4,5]

[5,6,7,8,9]

Lists have at least one common member -5
"""
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

for i in a:
    if i in b:
        print(i)

[i for i in a if i in b]
print(i)


# Another approach

def common_numbers(x, y):
    a_set = set(a)
    b_set = set(b)

    # check length
    if len(a_set.intersection(b_set)) > 0:
        return a_set.intersection(b_set)
    else:
        return "no common elements"


x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 8, 9]
print(common_numbers(x, y))

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9]
print(common_numbers(x, y))
