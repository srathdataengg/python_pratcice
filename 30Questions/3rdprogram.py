"""
Write a program to create, concatenate and print a string and accessing sub-string from a given string
"""
print("Enter two string to perform operations")
s1=str(input("Enter first string"))
s2=str(input("Enter seconf string"))
print(type(s1),type(s2));
print("first string:-",s1)
print("second string:-",s2);
print("Concaternate 2 strings",s1+s2);
print("Substring of given string:",s1[1:4]);
print("Substring of given string",s2[2:5]);