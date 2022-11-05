#Pattern Problem 5
# Resembles inverted equilateral traingle or pyramid.
#Demo eg:
"""
* * * * *
 * * * *
  * * *  
   * * 
    *
"""
# Code -->
rows = int(input("Enter the vertical height as number of rows"))
for i in range(rows):
    for j in range(i):    # Prints space
        print(" ",end='')
    for k in range(rows-i):       # Prints asterik
        print("* ",end='')
    print()

