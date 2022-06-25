
x = pow(10, 9) + 7
#
# n = 1
# print(n)
# ss =[]
# for n in range(10):
# 	for i in range(1, 11):
# 		ns = str(n)
# 		s = ''
# 		for j in ns:
# 			j = int(j)
# 			s += str(j + 1)
# 		n = int(s)
# 	ss.append(s)
# for i in range(len(ss)):
# 	print(i, ss[i])
# print(ss)
# ss = sorted(list(ss))
# print(''.join(ss))
# seseg

# def fast_pow2(n):
# 	if n == 0:
# 		return 1
# 	elif n % 2:
# 		return (2 * fast_pow2(n - 1)) % x;
# 	else:
# 		nn = fast_pow2(n // 2)
# 		return (nn * nn) % x


for t in range(int(input())):
	n, m = map(int, input().split())
	d = [0 for i in range(10)]
	dc = [0 for i in range(10)]
	for i in str(n):
		i = int(i)
		d[i] += 1
	for i in range(m % 10):
		for j in range(10):
			dc[j] = d[(j + 9) % 10]
		dc[1] = (dc[1] + d[9]) % x
		for j in range(10):
			d[j] = dc[j]
	for i in range(m // 10):
		dc[0] = (d[0] + d[9]) % x
		dc[1] = (d[0] + d[1] + d[9]) % x
		dc[2] = (d[1] + d[2]) % x
		dc[3] = (d[2] + d[3]) % x
		dc[4] = (d[3] + d[4]) % x
		dc[5] = (d[4] + d[5]) % x
		dc[6] = (d[5] + d[6]) % x
		dc[7] = (d[6] + d[7]) % x
		dc[8] = (d[7] + d[8]) % x
		dc[9] = (d[8] + d[9]) % x
		for i in range(10):
			d[i] = dc[i]
	last = sum(d)
	print(last % x)
