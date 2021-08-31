##
#    author:  kostya
#    created: 2021-08-01 17:28:01
#    modified 2021-08-01 17:46:37
##

for t in range(int(input())):
	n = int(input())
	p = list(input())
	p = list(map(int, p))
	m = list(input())
	m = list(map(int, m))
	for i in range(n):
		if m[i] == 0:
			continue
		if i == 0:
			if p[0] == 0:
				m[i]=0
				p[0] = 2
		if m[i] != 0 and i != 0 and p[i - 1] == 1:
			m[i]=0
			p[i - 1] = 2
		elif m[i] != 0 and p[i] == 0:
			m[i]=0
			p[i] = 2
		elif m[i] != 0 and i + 1 < n and p[i + 1] == 1:
			m[i]=0
			p[i+1] = 2
	print(p.count(2))
