"""
Swapping of 2 numbers using python
--5,6 --> 6,5

"""


def swap(a, b):
    a, b = b, a
    return (a, b)


print(swap(5, 6))


def swap1(a, b):
    sum = a + b
    b = a
    a = sum - b
    return (a, b)


print(swap1(5, 6))
