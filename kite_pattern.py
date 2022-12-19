# Program to print a pattern of kite using aestrik
"""
Demo eg-->
  *  
     
*   *
     
  *  
"""
# Code -->

for i in range(5):
	if i==0 or i==4:
		for j in range(5):
			if j==2:
				print('*',end='')
			else:
				print(' ',end='')
		print()
	elif i==1 or i==3:
		for k in range(5):
			print(' ',end='')
		print()
	else:
		for l in range(5):
			if l==0 or l==4:
				print('*',end='')
			else:
				print(' ',end='')
		print()

