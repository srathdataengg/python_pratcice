"""
Write a Python program to count the number of strings where the string length is 2 or more and the first and last
character are same from a given list of strings

Sample Output

['abc', 'xyz', 'aba', '1221']

First and Last Character are same : 2

"""

word = ["madem", "3643", "apple", "3756"]
count = 0
for w in word:
    if len(w) > 1 and w[0] == w[-1]:
        count += 1
print(count)
