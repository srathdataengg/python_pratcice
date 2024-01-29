"""
find k most frequent elemnt of an array
# Input array = [1,1,1,2,3,3] k =2
o/p - [1,2]
"""


def k_most_element(inout_array, k):
    base_dict = dict()
    final_set = set()
    for i in inout_array:
        if i in base_dict:
            base_dict[i] += 1
            print(base_dict)
            if base_dict[i] >= k:
                final_set.add(i)


        else:
            base_dict[i] = 1

    return final_set


print(k_most_element(['a', 'a', 'a', 'b', 'b', 'c', 'd'], 2))
