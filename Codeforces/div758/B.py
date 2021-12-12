##
#	Author:		antikostya
#	Created:	2021-12-11 13:05:10
#	Modified:	2021-12-11 13:42:33
##


def inp():
	return list(map(int, input().split()))

def next(a):
	if a >= 0:
		return a + 1
	else:
		return a - 1

for _t in range(int(input())):
	n, a, b = inp()
	if abs(a - b) > 1 or n < 3:
		print(-1)
		continue
	i = 2
	if a >= b:
		ans = [0, 1]
		s = -1
	else:
		ans = [0, -1]
		s = 1
	for i in range(2, n):
		if ans[-1] > 0 and a > 0:
			ans.append(ans[-1] - i)
			a -= 1
		elif ans[-1] < 0 and b > 0:
			ans.append(ans[-1] + i)
			b -= 1
		else:
			ans.append(next(ans[-1]))
	if a > 0 or b > 0:
		print(-1)
		continue
	mi = min(ans)
	ans = [i - mi + 1 for i in ans]
	print(*ans)
