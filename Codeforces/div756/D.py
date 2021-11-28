##
#	Author:		antikostya
#	Created:	2021-11-25 17:27:49
#	Modified:	2021-11-25 18:55:10
##

inc = []
hm = dict()

def inp():
	return list(map(int, input().split()))

def dfs(v):
	for i in inc[v]:
		if not hm[v] < hm[i]:
			return False
		if dfs(i) == False:
			return False
	return True

for _ in range(int(input())):
	n = int(input())
	b = inp()
	p = inp()
	# inc = [[] for i in range(n)]
	root = None
	for i in range(n):
		if b[i] == i + 1:
			root = i
			break
	# for i in range(n):
	# 	if b[i] == i + 1:
	# 		root = i
	# 		continue
	# 	inc[b[i] - 1].append(i)
	# hm = {p[i] - 1: i for i in range(n)}
	# if not dfs(root):
		# print(-1)
		# continue
	ok = True
	last = 0
	w = [-1] * n
	w[root] = 0
	path = [0] * n
	if p[0] != root + 1:
		print(-1)
		continue
	for i in range(1, n):
		parent = b[p[i] - 1] - 1
		if w[parent] == -1:
			print(-1)
			ok = False
			break
		w[p[i] - 1] = last - path[parent] + 1
		path[p[i] - 1] = path[parent] + w[p[i] - 1]
		last += 1
	if ok:
		print(*w)
	
