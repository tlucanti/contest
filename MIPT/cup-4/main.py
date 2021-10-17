##
#	Author:		antikostya
#	Created:	2021-10-10 16:10:53
#	Modified:	2021-10-10 16:20:30
##

mult = []


def from_fab(n):
	ans = 0
	for i in range(len(n)):
		ans += mult[i + 1] * n[i]
	# print(ans)
	return ans


def to_fab(n):
	ans = [0] * 20000
	for i in range(len(mult) - 1, -1, -1):
		ans[i] = n // mult[i]
		n %= mult[i]
	return ans


mult = [1] * 20000
for i in range(1, len(mult)):
	mult[i] = mult[i - 1] * i

for t in range(int(input())):
	_ = int(input())
	a = list(map(int, input().split()))[::-1]
	_ = int(input())
	b = list(map(int, input().split()))[::-1]
	ans = to_fab(from_fab(a) * from_fab(b))[::-1]
	if ans.count(0) == len(ans):
		print(0)
		continue
	for i in range(len(ans)):
		if ans[i] != 0:
			ans = ans[i:-1]
			break
	print(*ans)
