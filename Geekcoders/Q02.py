"""
find a non- negative integere that is not in that array.

Ex:- i/p - [0,1,2,3,4,5,7,8,9]
o/p - 6
"""

l = [0, 1, 2, 3, 4, 5, 7, 8, 9]
l.sort()

for i in range(len(l)-1):
    if l[i] + 1 not in l:
        print("number not present", l[i] + 1)
