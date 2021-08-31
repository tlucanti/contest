##
#    author:  kostya
#    created: 2021-08-01 19:20:38
#    modified 2021-08-01 19:23:40
##

for t in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	ma = 1
	cu = -1
	for m in range(2, 100):
		cu = a[0] % m
		cnt = 0
		for i in range(n):
			if a[i] % m == cu:
				cnt += 1
				ma = max(ma, cnt)
			else:
				cu = a[i] % m
				cnt = 1
	print(ma)



