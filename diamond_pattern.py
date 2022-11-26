# Program to a pattern which resembles the shape of a diamond
"""
Demo eg:-
  *
 * *
*   *
 * *
  *
"""
for i in range(5):
	if i ==0 or i==4:
		for j in range(5):
			if j ==2:
				print('*',end='')
			else:
				print(' ',end='')
		print()
	elif i ==1 or i==3:
		for k in range(5):
			if k ==1 or k==3:
				print('*',end='')
			else:
				print(' ',end='')
		print()
	else:
		for l in range(5):
			if l==0 or l==4:
				print('*',end='')
			else:
				print(' ',end='')
		print()