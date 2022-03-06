# @Author: tlucanti
# @Date:   2022-03-04 18:30:47
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-04 18:38:06


def inp():
	return list(map(int, input().split()))


_It = int(input())
for _ in range(_It):
	n, s = inp()
	print(s // (n * n))

