
def sgn(n):
	if n > 0:
		return 1
	return -1

def gcd(_a, _b):
	if _b == 0:
		return _a
	return gcd(_b, _a % _b)

n, m = map(int, input().split())
p = list(map(int, input().split())) # n
q = list(map(int, input().split())) # m
if n > m:
	sign = '-' if sgn(p[0] * q[0]) == -1 else ''
	print(sign + 'Infinity')
elif m > n:
	print('0/1')
else:
	sign = '-' if sgn(p[0] * q[0]) == -1 else ''
	p[0] = abs(p[0])
	q[0] = abs(q[0])
	_gcd = gcd(p[0], q[0])
	print(f'{sign}{p[0] // _gcd}/{q[0] // _gcd}')
