"""
Write a Python program to find the list of words that are longer than n from a given list of words
"""
n = 4
str = "Find the List of Words that are Longer than n from a given List of Words"

new_list = []

text = str.split(" ")
print(text)

for x in text:
    #print(x)
    if len(x) > n:
        new_list.append(x)
print(new_list)


