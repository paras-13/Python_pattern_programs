# Program to print a pattern of equilateral triangle or pyramid using alphabets
"""
Using alphabets in ascending order.
Demo eg:
    A
   B B
  C C C
 D D D D
E E E E E
"""
print("----------------------------------------------------")
print("In ascending order")
print("----------------------------------------------------")

#Code -->
rows = int(input("Enter the vertical height as number of rows"))
Ascii = 65
for i in range(rows):
    for j in range(rows-(i+1)):
        print(" ",end = "")
    for k in range(i+1):
        print(f"{chr(Ascii)} ",end = "")
    Ascii+=1
    print()

print("-------------------------------------------------")
print("In descending order")
print("-------------------------------------------------")
"""
Using alphabets in descending order
Demo eg:

E E E E E 
 D D D D
  C C C
   B B
    A
"""
# Code-->
Ascii = 64 + rows
for p in range(rows):
    for q in range(p):
        print(" ",end = "")
    for r in range(rows-p):
        print(f"{chr(Ascii)} ",end = "")
    Ascii-=1
    print()