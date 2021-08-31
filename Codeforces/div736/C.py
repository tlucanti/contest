##
#    author:  kostya
#    created: 2021-08-01 17:28:05
#    modified 2021-08-01 18:38:39
##

n, m = map(int, input().split())
inc = [set() for i in range(n)]
cnt = 0
for i in range(m):
	u, v = map(int, input().split())
	u, v = min(u, v), max(u, v)
	if len(inc[u]) == 0:
		cnt += 1
	inc[u].update((v,))
m = int(input())
for i in range(m):
	d = input().split()
	if d[0] == '3':
		print(n - cnt)
	else:
		u, v = map(int, d[1:])
		u, v = min(u, v), max(u, v)
		if d[0] == '1':
			if len(inc[u]) == 0:
				cnt += 1
			inc[u].update((v,))
		else:
			inc[u].remove(v)
			if len(inc[u]) == 0:
				cnt -= 1
