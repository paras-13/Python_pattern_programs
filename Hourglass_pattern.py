# Program to print a pattern of hourglass using aestrik in python

# Hourglass pattern
"""
Demo eg -->
* * * * * *
 * * * * *
  * * * *
   * * *  
    * * 
     *
     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
"""
# Code -->
def regular():
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(n-i):
            print("* ",end = "")
        print()
def invert():
    for i in range(n):
        for j in range(n-(i+1)):
            print(" ",end="")
        for k in range(i+1):
            print("* ",end = "")
        print()
n = int(input("Enter a number"))
regular()
invert()