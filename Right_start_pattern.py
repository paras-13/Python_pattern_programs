# Program to print a right start pattern
"""
Demo
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
"""
row = 11
a,b=1,0
for i in range(row):
    if i<=5:
        for j in range(i+a):
            print("* ",end="")
        print()
    else:
        for k in range(i-(a+b)):
            print("* ",end="")
        print()
        b+=2