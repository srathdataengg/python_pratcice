"""
Write a program to convert 2 list into dict.
list1 = ['Soumya','virat','dhoni']
list2 = ['234,'345','456']

"""

def list_to_dict():
    keys=['Soumya','Virat','Dhoni']
    values=[234,345,456]
    result=dict(zip(keys,values))
    print(result)

list_to_dict()

def dict_to_tuple():
    x= {'Soumya': 234, 'Virat': 345, 'Dhoni': 456}

    for i in x.items():
        print(i)

dict_to_tuple()