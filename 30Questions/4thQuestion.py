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
#print(my_list)

"""
We can use remove() method to remove the given item or pop() method to remove an item at the given index
The pop() method removed and returns the last item if the index is not provided, This helps us implements
lists as stacks(first in ,last out data structure)

Syntax of list pop()
list.pop(index)

The pop() method takes a single argument (index).
The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
If the index passed to the method is not in range, it throws IndexError: pop index out of range exception.
"""

prime_numbers = [1,3,5,7,11,13]

removed_numbers = prime_numbers.pop(3)

print("Removed items :-",removed_numbers)
print("prime numvbers:-",prime_numbers)

given_list =['Python','Scala','Java','C++']

#removed_list = given_list.pop(3);

print("Complete list :-",given_list);
#print("After removed element:-",removed_list);

# pop() without an index and for negative indices
# remove and return the last item
print('When index is not passed')
print('return value:-',given_list.pop())
print('Updated list',given_list)

print('return value :-',given_list.pop(-3)) # it will pop that particular value
print('upddated list:-',given_list) # it will return the updated list after pop out
