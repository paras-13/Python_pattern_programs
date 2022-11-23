# Program to print a left start pattern
"""
Demo -->
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
#Code -->
row = 11
for i in range(1,row+1):
  if i == 1 or i == 11:
    for j in range(10):
      print(" ",end="")
    print("* ",end="")
    print()
  elif i==2 or i==10:
    for k in range(8):
      print(" ",end="")
    print("* "*2,end="")
    print()
  elif i == 3 or i==9:
    for l in range(6):
      print(' ',end="")
    print("* "*3,end="")
    print()
  elif i==4 or i==8:
    for m in range(4):
      print(" ",end="")
    print("* "*4,end="")
    print()
  elif i==5 or i==7:
    for n in range(2):
      print(" ",end="")
    print("* "*5,end="")
    print()
  else:
    print("* "*6,end="")
    print()
      
      


