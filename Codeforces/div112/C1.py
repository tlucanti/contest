for t in range(int(input())):
	m = int(input())
	a = [list(map(int, input().split())), list(map(int, input().split()))]

	left_cum = [0]*m
	righ_cum = [0]*m
	left_cum[0] = a[1][0]
	righ_cum[-1]= a[0][-1]
	for i in range(1, m):
		left_cum[i] = left_cum[i-1] + a[1][i]
	for i in range(m-2, -1, -1):
		righ_cum[i] = righ_cum[i+1] + a[0][i]
	righ_cum.append(0)
	ans = righ_cum[1]
	for i in range(1, m):
		ans = min(max(righ_cum[i+1], left_cum[i-1]), ans)
	print(ans)
