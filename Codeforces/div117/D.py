##
#	Author:		antikostya
#	Created:	2021-11-22 12:27:48
#	Modified:	2021-11-22 14:14:40
##

for _ in range(int(input())):
	a, b, x = map(int, input().split())
	for i in range(20):
		a = abs(a - b)
		print(a, b)
