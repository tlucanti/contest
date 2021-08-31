st = set()



def dfs(a, b, i):
	a1 = a * 2
	a2 = str(a)
	a2 = a2.replace('0', 'O')
	a2 = a2.replace('1', '0')
	a2 = a2.replace('O', '1')
	a2 = int(a2, 2)
	if a1 == b or a2 == b:
		return i
	i1, i2 = 9999999, 9999999
	if a1 not in st:
		st.update((a1))
		i1 = dfs(a1, b, i + 1)
	if a2 not in st:
		st.update((a2))
		i2 = dfs(a2, b, i + 1)
	return max(i1, i2)

for t in range(int(input())):
	a, b = input().split()
	i = dfs(a, b, 0)
	st = set()
	if i == 9999999:
		i = 'IMPOSSIBLE'
	print(f'Case #{t + 1}: {i}')