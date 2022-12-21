# Program to print a pattern of cross using pattern printing with aestrick *

#Pattern 
"""
Demo eg -->
*   *
 * *
  *
 * *
*   *
"""
# Code -->
for i in range(5):
	if i==0 or i==4:
		for j in range(5):
			if j ==0 or j ==4:
				print('*',end='')
			else:
				print(' ',end='')
		print()
	elif i==1 or i==3:
		for j in range(5):
			if j==1 or j==3:
				print('*',end='')
			else:
				print(' ',end='')
		print()
	else:
		for l in range(5):
			if l==2:
				print('*',end='')
			else:
				print(' ',end='')
		print()
