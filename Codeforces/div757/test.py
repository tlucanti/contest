import itertools

a = [26564,26265526,232343,264264,2643432646326423,42354523,54,54642,6]
# a = [1, 2, 3, 4, 5, 6]
ar = [1]
for i in range(1, len(a)):
	ar.append(ar[-1] ^ a[i])
print(ar)
exit(0)


ans = 0
nums = dict()
for i in range(1, len(a) + 1):
	ai = 0
	for comb in itertools.combinations(a, i):
		comb = list(comb)
		aj = 0
		for j in comb:
			aj ^= j
		ai += aj
		nums[aj] = nums.get(aj, 0) + 1
		print(comb, ': ', aj, sep='')
	ans += ai
print(nums)
_a = 0
for i in a:
	_a |= i
print(_a * pow(2, len(a) - 1))
print(ans)
