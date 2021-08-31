for t in range(int(input())):
	m = int(input())
	a = [list(map(int, input().split())), list(map(int, input().split()))]
	dp1 = [[[0, 0] for i in range(m)], [[0, 0] for i in range(m)]]
	dp1[0][0][0] = a[0][0]
	dp1[1][0][0] = a[0][0] + a[1][0]
	dp1[1][0][1] = 0
	for i in range(1, m):
		dp1[0][i][0] = dp1[0][i-1][0] + a[0][i]
	for i in range(1, m):
		if dp1[0][i][0] >= dp1[1][i-1][0]:
			dp1[1][i][0] = dp1[0][i][0] + a[1][i]
			dp1[1][i][1] = i
		else:
			dp1[1][i][0] = dp1[1][i-1][0] + a[1][i]
			dp1[1][i][1] = dp1[1][i-1][1]

	ans1 = dp1[-1][-1][0]
	turn = dp1[-1][-1][1]
	for i in range(turn + 1):
		a[0][i] = 0
	for i in range(turn, m):
		a[1][i] = 0

	dp1 = [[[0, 0]]*m, [[0, 0]]*m]
	dp1[0][0][0] = a[0][0]
	dp1[1][0][0] = a[0][0] + a[1][0]
	dp1[1][0][1] = 0
	for i in range(1, m):
		dp1[0][i][0] = dp1[0][i-1][0] + a[0][i]
	for i in range(1, m):
		if dp1[0][i][0] > dp1[1][i-1][0]:
			dp1[1][i][0] = dp1[0][i][0] + a[1][i]
			dp1[1][i][1] = i
		else:
			dp1[1][i][0] = dp1[1][i-1][0] + a[1][i]
			dp1[1][i][1] = dp1[1][i-1][1]

	ans2 = dp1[-1][-1][0]
	print(ans2)
