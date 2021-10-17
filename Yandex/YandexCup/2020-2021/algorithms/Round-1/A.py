##
#	Author:		antikostya
#	Created:	2021-10-03 19:32:28
#	Modified:	2021-10-03 19:38:51
##

a = input()
b = input()
a = a.replace('one', '1')
a = a.replace('zero', '0')
b = b.replace('one', '1')
b = b.replace('zero', '0')
a = int(a, 2)
b = int(b, 2)
if a > b:
	print('>')
elif b > a:
	print('<')
else:
	print('=')
