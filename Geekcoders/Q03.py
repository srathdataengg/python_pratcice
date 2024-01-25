"""
check a string is palindrome or not
str = 'aba'
"""


def check_pallindrome(str):
    print(str)
    if str == str[::-1]:
        return "the string is palindrome"
    else:
        return "the string is not palindrome"


str = "aba"
print(check_pallindrome(str))


def check_using_loop(str):
    rev_str = ""

    for i in str:
        rev_str = i + rev_str
    print("reverse string", rev_str)

    if str == rev_str:
        return "string is palindrome"
    else:
        return "string is not palindrome"


print(check_using_loop(str="malayalam"))
