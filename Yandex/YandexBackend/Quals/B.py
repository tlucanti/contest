
import functools

def reduce(a, b):
	if a == -1 or b == -1:
		return max(a, b)
	return a | b

n = int(input())
ans = []
if n == 1:
	print(0)
	exit(0)
for i in range(n):
	s = list(map(int, input().split()))
	ans.append(functools.reduce(reduce, s))
print(*ans)
