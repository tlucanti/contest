def dn(x):
	return len(str(x))

def sn(s):
	cmp = 0
	s = list(s)
	for i in range(len(s) - 1, -1, -1):
		if s[i] != '9':
			s[i] = str(int(s[i]) + 1)
			cmp = 1
			break
		else:
			s[i] = '0'
	s = ''.join(s)
	if not cmp:
		s = '1' + s
	return s

def strcmp(s1, s2):
	if len(s1) > len(s2):
		return 1
	if len(s1) == len(s2) and s1 > s2:
		return 1
	return 0

for t in range(int(input())):
	sm, prev, ans = 0, '', 0
	n = int(input())
	s = input().split()
	sm = len(s[0])
	prev = s[0]
	for j in range(1, n):
		x = s[j]
		nct = sn(prev);
		nct_prv = nct[:len(x)]
		prv = prev[:len(x)]
		prv1 = x;
		while len(x) < sm:
			x += '0'
			ans += 1
		if strcmp(prv1, prv):
			sm = len(x)
			prev = x
		elif len(prv1) == len(prv) and prv1 == prv:
			if nct_prv != prv1:
				x += '0'
				ans += 1
				prev = x
				sm = len(x)
			else:
				x = nct
				prev = x
				sm = len(x)
		else:
			x += '0'
			ans += 1
			prev = x
			sm = len(x)
	print(f'Case #{t + 1}: {ans}')
