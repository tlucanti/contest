##
#    author:  kostya
#    created: 2021-08-09 17:48:50
#    modified 2021-08-09 18:16:23
##

for t in range(int(input())):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	idx = dict()
	srt = list(sorted(a))
	for i in range(n):
		idx[srt[i]] = i
	j = idx[a[0]]
	p = 1
	for i in range(1, n):
		if j + 1 >= n or a[i] != srt[j + 1]:
			p += 1
			j = idx[a[i]]
		else:
			j += 1
	if p > k:
		print('NO')
	else:
		print('YES')

	
