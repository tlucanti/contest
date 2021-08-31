import sys
sys.setrecursionlimit(100000)


def dfs(n):
	mat[n] = 1
	stack.append(n + 1)
	for i in inc[n]:
		if mat[i] == 1:
			return stack, i + 1
		elif mat[i] == 0:
			ans = dfs(i)
			if ans is not None:
				return ans
	stack.pop()
	mat[n] = 2
	return None


n, m = map(int, input().split())
inc = [[] for _ in range(n)]
mat = [0 for _ in range(n)]
stack = []
for i in range(m):
	start, end = map(int, input().split())
	inc[start - 1].append(end - 1)

for i in range(n):
	if mat[i] == 0:
		ret = dfs(i)
		if ret is not None:
			print('YES')
			# print(ret)
			print(*ret[0][ret[0].index(ret[1]):])
			break
if ret is None:
	print('NO')
