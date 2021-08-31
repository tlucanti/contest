
def d(x):
	s = 0
	for i in range(1, x + 1):
		if x % i == 0:
			s += i
		i += 1
	return s


m = pow(10, 5)
m += 2
reseto = [0 for i in range(m)]
for i in range(1, m + 1):
	# print(i)
	# if i % pow(10, 3) == 0:
	# 	print(i)
	for j in range(i, m, i):
		reseto[j] += i


print(max(reseto))

# for t in range(int(input())):
# 	n = int(input())
for n in range(100):
	x = None
	print(n, end=' ')
	try:
		x = reseto.index(n)
		print(x)
	except ValueError:
		print(-1)
