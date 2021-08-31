
m, n = map(int, input().split())
s = list(map(int, input().split()))
mat = [False for _ in range(m + 1)]
cur_mat = mat.copy()
for i in range(m + 1):
	mat[i] = i == s[0]
mat[0] = True
for j in range(1, n):
	for i in range(m + 1):
		cur_mat[i] = mat[i] or (False if i < s[j] else mat[i - s[j]])
	del mat
	mat = cur_mat
	cur_mat = [False for _ in range(m + 1)]
for i in range(m, -1, -1):
	if mat[i]:
		print(i)
		break
