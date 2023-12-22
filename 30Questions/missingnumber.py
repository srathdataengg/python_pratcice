"""
find missing number from a given array(using summation or xor method)
[1,2,4,5,6,7]

Sum of n natural
----------------  - sum(A)
numbers 
n*(n+1)/2
"""

def get_missing_summation(a):
    n = a[-1]
    sum_value =0
    total = n*(n+1)//2
    sum_value=sum(a)
    print(total-sum_value)




a = [1,2,4,5,6,7]

get_missing_summation(a)