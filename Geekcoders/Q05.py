"""
factorial of a given number
-5 = 5 * 4 *3 *2 *1
"""


def factorial_number(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i
        print(i, fact)
    return fact


print(factorial_number(5))
