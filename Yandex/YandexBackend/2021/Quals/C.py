##
#	Author:		antikostya
#	Created:	2021-11-27 13:34:45
#	Modified:	2021-11-27 14:17:36
##


def inp():
	return list(map(int, input().split()))

n, m = inp()
a, b = inp()[::-1], inp()
floors = [a[0]]
last = a[0]
for i in range(1, n):
	fl = a[i] - last
	if fl > 0:
		floors.append(a[i] - last)
		last = a[i]
floors.sort()
b.sort()
ans = 0
# print(b)
# print(floors)
i, j = 0, 0
while i < len(b) and j < len(floors):
	if b[i] > floors[j]:
		j += 1
		continue
	ans += 1
	i += 1
	j += 1
print(ans)
