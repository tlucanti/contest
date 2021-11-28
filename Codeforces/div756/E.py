##
#	Author:		antikostya
#	Created:	2021-11-25 17:27:49
#	Modified:	2021-11-25 19:41:33
##
import sys
sys.setrecursionlimit(1200000)

def inp():
	return list(map(int, input().split()))

inc = list()
fr = set()
path = list()

def dfs1(p, parent):
	if p in fr:
		return 0
	steps = None
	for i in inc[p]:
		if i == parent:
			continue
		branch = dfs1(i, p)
		if branch is not None:
			if steps is None:
				steps = branch + 1
			else:
				steps = min(steps, branch + 1)
	path[p] = steps
	return steps


def dfs2(p, parent):
	if path[p] is None:
		path[p] = path[parent] + 1
	else:
		path[p] = min(path[p], path[parent] + 1)
	for i in inc[p]:
		if i == parent:
			continue
		dfs2(i, p)

def dfs3(p, parent, turn):
	if len(inc[p]) == 1 and turn < path[p] and p != 0:
		return True
	for i in inc[p]:
		if i == parent:
			continue
		ok = dfs3(i, p, turn + 1)
		if ok:
			return True
	return False

for _ in range(int(input())):
	input()
	n, k = inp()
	fr = {i - 1 for i in inp()}
	inc = [[] for i in range(n)]
	for i in range(n - 1):
		_a, _b = inp()
		_a -= 1
		_b -= 1
		inc[_a].append(_b)
		inc[_b].append(_a)
	path = [None] * n
	for f in fr:
		path[f] = 0
	dfs1(0, 0)
	dfs2(0, 0)
	if dfs3(0, 0, 0):
		print('YES')
	else:
		print('NO')
