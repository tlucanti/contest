##
#	Author:		antikostya
#	Created:	2021-11-23 17:50:31
#	Modified:	2021-11-23 18:30:04
##

def inp():
	return list(map(int, input().split()))

for _ in range(int(input())):
	n = int(input())
	a = inp()
	if a == a[::-1]:
		print('YES')
		continue
	le = 0
	ri = n - 1
	ok = False
	while le < ri:
		if a[le] != a[ri]:
			dl = [A for A in a if A != a[le]]
			if dl == dl[::-1]:
				ok = True
				break
			dl = [A for A in a if A != a[ri]]
			if dl == dl[::-1]:
				ok = True
				break
			break
		le += 1
		ri -= 1
	if ok:
		print('YES')
	else:
		print('NO')
