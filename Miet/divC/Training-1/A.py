
n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in range(n):
	d[a[i]] = d.get(a[i], 0) + 1
s = set(a)
scores = [0 for _ in range(len(s))]
for i in range(n):
	scores = [0 for _ in range(len(s))
	for j in range()