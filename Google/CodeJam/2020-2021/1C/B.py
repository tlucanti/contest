
def check_next(n, i, prev):
	next = str(prev + 1)
	size = len(next)
	if n[i:i + size] == '':
		return True
	if n[i:i + size] == next:
		return check_next(n, i + size, int(next))
	return False


def is_roar(n):
	if len(n) > 1 and check_next(n, 1, int(n[:1])):
		return True
	if len(n) > 2 and check_next(n, 2, int(n[:2])):
		return True
	if len(n) > 3 and check_next(n, 3, int(n[:3])):
		return True
	return False


for t in range(int(input())):
	n = int(input()) + 1
	while not is_roar(str(n)):
		n += 1
	print(f'Case #{t + 1}: {n}')
