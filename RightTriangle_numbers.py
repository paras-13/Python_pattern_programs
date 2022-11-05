#Forward Pyramid or right triangle pattern using numbers 
# Code
'''
Demo
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

#Code-->
size = 5
for i in range(size):
    for j in range(i+1):
        print(j+1," ",end="")
    print()

print("--------------------------------------------")
print("--------------------------------------------")
print("--------------------------------------------")

"""
Eg
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
size = 5
a = size
for i in range(size):
    for j in range(size-i):
        print(a-j," ",end="")
    a= a-1
    print()