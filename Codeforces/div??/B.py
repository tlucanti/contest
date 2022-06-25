
x = pow(10, 9) + 7


def A(n, k):
	ans = 1
	for i in range(n - k + 1, n + 1):
		ans = (ans * i) % x
	return ans


for t in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	bit = a[0]
	for i in a:
		bit &= i
	cnt = a.count(bit)
	if cnt < 2:
		print(0)
		continue
	print((A(cnt, 2) * A(n - 2, n - 2)) % x)
