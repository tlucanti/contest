# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-04 18:30:47
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-04 20:28:34


def inp():
	return list(map(int, input().split()))


n = int(input())
visited = [0] * n
weights = [0] * n
good = [0] * n
inc = [[] for _ in range(n)]
for i in range(n - 1):
	u, v = inp()
	u -= 1
	v -= 1
	inc[u].append(v)
	inc[v].append(u)


for i in range(n):
	if len(inc[i]) == 1:
		good[i] = 1
		weights[i] = 1
		neig = inc[i][0]
		if len(inc[neig]) > 1:
			good[neig] = 0
			weights[neig] = 1

for i in range(n):
	if len(inc[i]) == 2:
		if weights[i] != 0:
			continue
		weights[i] = 2
		good[i] = 1
		neg1 = inc[i][0]
		neg2 = inc[i][1]
		if weights[neg1] == 0:
			weights[neg1] = 1
			good[neg1] = 0
		if weights[neg2] == 0:
			weights[neg2] = 1
			good[neg2] = 0

for i in range(n):
	if weights[i] == 0:
		w = 0
		good[i] = 1
		for neig in inc[i]:
			if weights[neig] == 0:
				weights[neig] = 1
				good[neig] = 0
			w += weights[neig]
		weights[i] = w


print(sum(good), sum(weights))
print(*weights)
