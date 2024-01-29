"""
Reverse order of words
sentence = "this is soumyakanta"
soumyakanta is this
"""


def reverse(sentence):
    list_words = []
    words = sentence.split(" ")
    print(words)
    while (len(words)) > 0:
        word = words.pop()
        list_words.append(word)
    return " ".join(list_words)


print(reverse("this is soumyakanta"))


def reverse1():
    line = "hello welcome to python"
    reverse_line = line.split(" ")[::-1]
    return " ".join(reverse_line)


print(reverse1())
