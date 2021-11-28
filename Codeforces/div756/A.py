##
#	Author:		antikostya
#	Created:	2021-11-25 17:27:49
#	Modified:	2021-11-25 17:38:29
##

def inp():
	return list(map(int, input().split()))

even = ['2', '4', '6', '8']

for _ in range(int(input())):
	n = input()
	ok = False
	for e in even:
		if e in n:
			ok = True
			break
	if not ok:
		print(-1)
	elif n[-1] in  even:
		print(0)
	elif n[0] in even:
		print(1)
	else:
		print(2)
