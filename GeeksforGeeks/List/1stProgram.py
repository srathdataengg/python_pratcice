"""
Write a python program to interchange the 1st and last element in a list
"""

def swapList(my_list):
    list_size = len(my_list)

    temp = my_list[0]
    my_list[0]=my_list[list_size-1]
    my_list[list_size-1]=temp

    print(my_list)

swapList(my_list=[1,3,5])