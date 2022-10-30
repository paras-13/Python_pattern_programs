#Program to draw right angle triangle using English alphabets
"""
Demo-->
A
B B
C C C
D D D D
E E E E E
"""
#Code -->
row = int(input("Enter number of rows you want"))
ascii_num = 65
for i in range(row):
    for j in range(i+1):
        print(chr(ascii_num)," ",sep="",end="")
    ascii_num+=1
    print()

