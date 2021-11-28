import sys
sys.setrecursionlimit(10100)


def dp(n, m):
	if n > 0 and m > 0:
		if mat[n - 1][m] == -1:
			dp(n - 1, m)
		if mat[n][m - 1] == -1:
			dp(n, m - 1)
		mat[n][m] = max(mat[n][m - 1], mat[n - 1][m])
	elif n == 0 and m == 0:
		mat[n][m] = 0
	elif n == 0:
		if mat[n][m - 1] == -1:
			dp(n, m - 1)
		mat[n][m] = mat[n][m - 1]
	elif m == 0:
		if mat[n - 1][m] == -1:
			dp(n - 1, m)
		mat[n][m] = mat[n - 1][m]
	mat[n][m] += sc[n][m]


n, m = map(int, input().split())
mat = [[-1 for _ in range(m)] for __ in range(n)]
sc = [[] for _ in range(n)]
for i in range(n):
	sc[i] = list(map(int, input().split()))
dp(n - 1, m - 1)
print(mat[n - 1][m - 1])

