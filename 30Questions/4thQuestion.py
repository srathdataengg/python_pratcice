"""
Write a python script to create,append and remove lists in python
"""
#empty list
my_list =[]

#list with integers
int_list=[1,2,3,4]

# list with mixed data types
my_list1=[1,"Hello",3,4]

# A list can also have another list as an item. This is called a nested list
my_list = ["mouse",[8,4,6],['a']]

# We can add one item to a list using teh append() method or add several items using extend() method
# append can be used to add one value and for multple values can be added using extend()
odd =[1,3,5]

odd.append(7)
print(odd)

odd.extend([9,11,13])
print(odd)

# Delete/Remove list elements - we can delete one or more items from a list using the keyword del.
# It can even the delete the complete list. to delete we have to provide the position
my_list=['p','r','o','b','l','e','m']

# delete one item
#del my_list[2]
print(my_list)

# delete multiple items
#del my_list[1:4]
print(my_list)

# delete complete list
del(my_list)
print(my_list)