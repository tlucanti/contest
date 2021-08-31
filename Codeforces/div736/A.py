##
#    author:  kostya
#    created: 2021-08-01 17:27:54
#    modified 2021-08-01 17:40:11
##

nums = list(range(2,100))


def find(n):
	for i in nums:
		for j in nums:
			if i == j:
				continue
			if n % i == n % j:
				if i > n or j > n:
					continue
				print(*sorted([i, j]))
				return None


for t in range(int(input())):
	n = int(input())
	find(n)
