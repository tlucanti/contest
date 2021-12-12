##
#	Author:		antikostya
#	Created:	2021-11-28 17:20:23
#	Modified:	2021-11-28 20:03:28
##

def inp():
	return list(map(int, input().split()))


def dfs(ry, rx, parent):
	roots[ry] = rx
	for r in inc[ry]:
		if r == parent:
			continue
		dfs(r, rx, ry)


n, d = inp()
roots = list(range(n))
meets = [0] * n
inc = [[] for i in range(n)]
mx = 0
for i in range(d):
	x, y = inp()
	x -= 1
	y -= 1
	if meets[roots[y]] > meets[roots[x]]:
		x, y = y, x
	if roots[x] != roots[y]:
		meets[roots[x]] += meets[roots[y]] + 1
	dfs(roots[y], roots[x], -1)
	if roots[x] != roots[y]:
		inc[x].append(y)
		inc[y].append(x)
	mx = max(mx, meets[roots[x]])
	print(mx)
