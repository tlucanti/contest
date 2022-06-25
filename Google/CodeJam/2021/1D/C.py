
def solver(n, c):
	if c < n - 1 or c > 2 * n:
		ans = 'IMPOSSIBLE'
	elif c <= 2 * n - 2:
		ans = list(range(1, n + 1))
		ans[2 * n - c - 2:] = ans[2 * n - c - 2:][::-1]
	else:
		ans = 'idk'
	return ans


import itertools
def solver_slow(n, c):
	ans = []
	for i in itertools.permutations(range(1, n + 1)):
		if checker(n, list(i)) == c:
			return i
			ans.append(i)
	return 'IMPOSSIBLE' #if len(ans) == 0 else ans


def checker(n, s):
	cnt = 0
	for i in range(n - 1):
		m = min(s[i:])
		j = s[i:].index(m)
		j += i
		cnt += j - i + 1
		s[i:j + 1] = s[i:j + 1][::-1]
	return cnt

#
# for t in range(int(input())):
# 	n, c = map(int, input().split())
# 	ans1 = solver(n, c)
# 	ans2 = solver_slow(n, c)
# 	print(ans1, ans2)
	# if ans == 'IMPOSSIBLE':
	# 	print(ans)
	# else:
	# 	print(f'Case #{t + 1}: {" ".join(map(str, ans))}')
	# 	print(checker(n, ans))

from random import randint as r
for t in range(int(input())):
	# n = r(1, 5)
	# c = r(1, 5)
	n, c = map(int, input().split())
	# ans1 = solver(n, c)
	ans2 = solver_slow(n, c)
	if ans2 != 'IMPOSSIBLE':
		ans2 = ' '.join(map(str, ans2))
	print(f'Case #{t + 1}: {ans2}')
	continue

	print(ans1)
	print(ans2)
	continue
	if ans1 == 'IMPOSSIBLE' and ans2 == 'IMPOSSIBLE':
		continue
	elif ans1 == 'IMPOSSIBLE':
		print(n, c, ans1, ans2)
	elif ans2 == 'IMPOSSIBLE':
		print(n, c, ans1, ans2)
	else:
		if checker(n, list(ans1)) != checker(n, list(ans2)):
			print(n, c, ans1, ans2)
