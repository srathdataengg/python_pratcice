# Write a python program that will extract the common word from 2 string

def common_string():
    str1 = input("Enter the first string")
    str2 = input("Enter the second string")
    print(type(str1))
    s1 = set(str1) # type casting using set method to change str to set method
    print(type(s1))
    s2 = set(str2)

    lst = s1 & s2
    print(lst)

if __name__=="__main__":
    common_string()