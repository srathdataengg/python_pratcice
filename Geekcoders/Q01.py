"""
check if there are 2 numbers present in a list that there sum = 0
Ex:- [-1,1,2,-2,3,4,5]
"""


def add_num(l):
    if len(l) < 2:
        return False
    else:
        l1 = set(l)
        for i in l1:
            if -i in l1:
                return True
        return False


l = [-1, 1, 2, -2, 3, 4, 5]

print(add_num(l))
