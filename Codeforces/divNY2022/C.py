##
#	Author:		antikostya
#	Created:	2022-01-03 17:29:23
#	Modified:	2022-01-03 19:44:29
##

import sys

def flush():
	sys.stdout.flush()

t = int(input())
for _ in range(t):
	n = int(input())
	flush()
	ans = [-1] * n
	i = 0
	print('? 1')
	flush()
	a = int(input())
	flush()
	prev = 1
	done = 0
	while not done:
		print(f'? {a}')
		flush()
		new = int(input())
		if new == 0:
			sys.exit(0)
		flush()
		if prev != -1:
			ans[prev - 1] = new
		# print('>>', *ans)
		prev = new
		if (ans[new - 1] != -1):
			while ans[i] != -1:
				i += 1
				if i == n:
					done = 1
					print('!', *ans)
					flush()
					break
			a = i + 1
			prev = -1


