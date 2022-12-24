# Program to draw diamond shape pattern in python
"""
Demo eg:
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
def higher():
    for i in range(n):
        for j in range(n-(i+1)):
            print(" ",end="")
        for k in range(i+1):
            print("* ",end = "")
        print()
def lower():
    for i in range(n-1):
        for j in range(i):
            print(" ",end="")
        for k in range(n-(i+1)):
            print(" *",end = "")
        print()
n = int(input())
higher()
lower()