"""
Python dictionaries:-=
While indexing is used to access other data types in dictionary we use Keys .Keys can be used inside [] or  get method.
If we use the square brackets [],keyError is raised in case a key is not found in the dictionary.

Syntax :-
dict_var = {'key1':value1,'key2':value2,key3:value3}

Complexities of adding a value to dictionary:-
Time complexity:-o(1)/o(n)
Space complexity:-O(1)

Complexities of accessing a value in dictionary:-
Time complexity :- O(1)
Space complexity :- O(1)

Dictionary Methods:-

Method :--------- Description

dic.clear() ---- removes all the elements from dictionary
dict.copy() ---  returns a copy of the dictionary
dict.get(key,default="None) -- returns the value of specified key
dict.items() -- returns a list containing a tuple for each key,value pair
dict.keys() -- returns a list containing list of keys.
dict.values() -- returns a list containing list of values

"""

# get vs [] while retrieving values

sample_dict ={'name':'Soumyakanta','age':36}
print(sample_dict['name'])
print(sample_dict.get('age'))
print(sample_dict.get('address')) # o/p - None

dict2= sample_dict.copy()
print("Copy of sample_dict:-",dict2)
print(dict2.get('name'))
print(dict2.keys())
print(dict2.values())
print("items list :-",sample_dict.items())