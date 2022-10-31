#Pattern 2
# Resembles equilateral traingle or pyramid
#Demo eg:
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
rows = int(input("Enter the vertical height as number of rows"))
for i in range(rows):
    for j in range(rows-i):    # Prints space
        print(" ",end='')
    for k in range(i+1):       # Prints asterik
        print("* ",end='')
    print()
