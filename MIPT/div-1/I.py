##
#	Author:		antikostya
#	Created:	2021-09-22 10:38:00
#	Modified:	2021-09-22 11:59:14
##

def prop(d):
	if d <= 1:
		return 18 / 20
	elif d >= 20:
		return 0
	return (20 - d) / 20


d, m = map(int, input().split())
ad = input()

k, *ext = input().split()
k = int(k)
n = [1, 1, 1, 1, 1]
sign = [1, 1, 1, 1, 1]
for i in range(k):
	n[i] = int(ext[i][2:])
	sign[i] = 1 if ext[i][0] == '+' else -1

out = 0
total = n[0] * n[1] * n[2] * n[3] * n[4]
for i0 in range(1, n[0] + 1):
	if n[0] == 1:
		i0 = 0
	for i1 in range(1, n[1] + 1):
		if n[1] == 1:
			i1 = 0
		for i2 in range(1, n[2] + 1):
			if n[2] == 1:
				i2 = 0
			for i3 in range(1, n[3] + 1):
				if n[3] == 1:
					i3 = 0
				for i4 in range(1, n[4] + 1):
					if n[4] == 1:
						i4 = 0
					ans = i0*sign[0] + i1*sign[1] + i2*sign[2] + i3*sign[3] + i4*sign[4]
					ans += m
					d1 = (1/20 + prop(d - ans))
					if ad == 'plain':
						d1 = d1
					elif ad == 'adv':
						d1 = d1 + d1 - d1 * d1
					else:
						d1 = d1 * d1
					out += d1 / total

print(out)
