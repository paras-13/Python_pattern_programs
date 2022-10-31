# Aestrik pattern for right angle triangle
# Rows here actually represents the perpendicular length of the triangle.
# In Ascending order
# Demo example
'''
* 
* * 
* * *  
* * * *      
* * * * *        
'''
#Code
rows = int(input("Enter the number of rows you want your triangle should have"))
for i in range(rows):
    for j in range(i+1):
        print("* ",end="")    
    print()                      # For next line

print("----------------------------------------------------------------")
print()                                                         # For gap between both the patterns
print("---------------------------------------------------------------")
# To print this in reverse form or Descending order
#Demo example
'''
* * * * * 
* * * * 
* * * 
* *
*
'''
#Code
for l in range(rows):
    for m in range(rows-l):
        print("* ",end='')
    print()