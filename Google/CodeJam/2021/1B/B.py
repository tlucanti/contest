


for t in range(int(input())):
	n, a, b = map(int, ipnut().split())
	ar = list(map(int, input().split()))
	for i in range(20):
		mp = [0 for i in range(int(input()))]
		mp[i] = 1
		while mp != ar:
			for j in range(n - 1, -1, -1):
				if mp[j] < ar[]
