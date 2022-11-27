# Program to print a pattern of double diamond or joint diamond using aestrik.
"""
Demo Eg:
  *   *  
 * * * *
*   *   *
 * * * *
  *   *
"""

for i in range(5):
	if i==0 or i==4:
		for j in range(9):
			if j==2 or j ==6:
				print('*',end='')
			else:
				print(' ',end='')
		print()
	elif i==1 or i== 3:
		for k in range(9):
			if k==1 or k==3 or k==5 or k==7:
				print('*',end='')
			else:
				print(' ',end='')
		print()
	else:
		for l in range(9):
			if l ==0 or l==4 or l==8:
				print('*',end='')
			else:
				print(' ',end='')
		print()