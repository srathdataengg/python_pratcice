"""
Write a program to count the frequency of words in a string.

e.g. - Sheena loves eating apple and mango, her sister also loves eating apple and mango
"""
def freq_words():
    str = input("Enter a string")
    list =str.split()
    result_dict ={}

    for i in list:
        if i not in result_dict.keys():
            result_dict[i]=0
        result_dict[i]=result_dict[i] + 1
    print(result_dict)

freq_words()