"""
Write a program to print below triangle

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

n = int(input("Enter the value for triangle"))

for i in range(1,n,+1):
    for j in range(i):
        print("*",end="")
    print("")
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
    