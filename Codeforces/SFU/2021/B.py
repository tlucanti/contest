
def dfs(row, col, vec, turn):
	if turn == 4:
		return 0
	if mp[row][col] == 'T':
		return 1
	ans = 0
	if col > 0 and mp[row][col - 1] != '*' and vec != 'u':
		ans += dfs(row, col - 1, 'd', turn + (vec != 'd'))
	if col < m - 1 and mp[row][col + 1] != '*' and vec != 'd':
		ans += dfs(row, col + 1, 'u', turn + (vec != 'u'))
	if row > 0 and mp[row - 1][col] != '*' and vec != 'r':
		ans += dfs(row - 1, col, 'l', turn + (vec != 'l'))
	if row < n - 1 and mp[row + 1][col] != '*' and vec != 'l':
		ans += dfs(row + 1, col, 'r', turn + (vec != 'r'))
	return ans > 0

def bfs(row, col, vec, turn):


n, m = map(int, input().split())
mp = [input() for i in range(n)]
f = 'NO'
for i in range(n):
	if mp[i].count('S') > 0:
		ans = dfs(i, mp[i].index('S'), 'z', 0)
		if ans > 0:
			f = 'YES'
			break
print(f)

# for i in mp:
# 	print(''.join(i))
