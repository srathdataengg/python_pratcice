# Write a program to find the largest of 3 numbers

a = int(input("Enter the first value"))
b = int(input("Enter the second value"))
c = int(input("Enter the 3rd value"))

if (a>b) and (a>c):
    print("a is bigger:-",a)
elif(b >a) and (b>c):
    print("b is greater:-",b)
else:
    print("C is greater")

    
