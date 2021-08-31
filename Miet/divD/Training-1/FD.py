##
#    author:  kostya
#    created: 2021-07-31 14:12:13
#    modified 2021-07-31 14:17:46
##

for t in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	ai = [0] * n
	for i in range(n):
		ai[a[i] - 1] = i
	mai = mii = ai[0]
	for i in range(n):
		mai = max(ai[i], mai)
		mii = min(ai[i], mii)
		print(int(mai - mii == i), end='')
	print()
