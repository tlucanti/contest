##
#	Author:		kostya
#	Created:	2021-09-03 23:29:15
#	Modified:	2021-09-03 23:29:16
##

r, i, c = [int(input()) for i in range(3)]
if i == 0:
	if r != 0:
		print(3)
	else:
		print(c)
elif i == 1:
	print(c)
elif i == 4:
	if r != 0:
		print(3)
	else:
		print(4)
elif i == 6:
	print(0)
elif i == 7:
	print(1)
else:
	print(i)



