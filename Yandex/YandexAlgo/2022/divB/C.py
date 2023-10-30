##
#	Author:		kostya
#	Created:	2021-09-03 23:09:25
#	Modified:	2021-09-03 23:29:28
##

def is_leap(y):
	if y % 400 == 0:
		return True
	if y % 100 == 0:
		return False
	if y % 4 == 0:
		return True
	return False


x, y, z = map(int, input().split())
American = True
European = True
if y > 12:
	European = False
if x > 12:
	American = False
if x == y:
	American == False
	European = False

if American and European:
	print(0)
else:
	print(1)

