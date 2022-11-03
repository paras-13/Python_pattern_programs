# Program to print a pattern of equilateral triangle or pyramid using numbers
"""
Using numbers in ascending order.
Demo eg:
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
"""
# Code-->
print("----------------------------------------------------")
print("In ascending order")
print("----------------------------------------------------")
rows = int(input("Enter the vertical height as number of rows"))
for i in range(rows):
    for j in range(rows-(i+1)):
        print(" ",end = "")
    for k in range(i+1):
        print(f"{i+1} ",end = "")       # Using f string
    print()


print("-------------------------------------------------")
print("In descending order")
print("-------------------------------------------------")
"""
Using numbers in descending order
Demo eg:

5 5 5 5 5 
 4 4 4 4
  3 3 3
   2 2
    1
"""
for p in range(rows):
    for q in range(p):
        print(" ",end = "")
    for r in range(rows-p):
        print(f"{rows-p} ",end = "")       # Using f string
    print()





