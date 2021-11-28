##
#	Author:		antikostya
#	Created:	2021-10-24 12:33:40
#	Modified:	2021-10-24 15:34:35
##

n = int(input())
ar = list(map(int, input().split()))
d = {ar[i]: i for i in range(n)}
ans = set(ar)
for xx in range(n * 2):
	dcp = d.copy()
	for i in dcp:
		nxt = d.get(i ^ xx, None)
		if nxt is None:
			continue
		if (d[i] < nxt and i < ar[nxt]) or (d[i] > nxt and i > ar[nxt]):
			ans.add(xx)
			d[xx] = nxt
ans.add(0)
print(*sorted(ans))
