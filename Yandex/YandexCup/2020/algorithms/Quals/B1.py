st = input()
mp = ''
c = 0
for i in range(1, len(st) - 1):
	if st[i - 1] == st[i]:
		if len(mp) in {0, 3}:
			mp = st[i - 1: i + 1]
		else:
			if st[i - 1:i + 1] < mp:
				mp = st[i - 1:i + 1] 
	elif st[i - 1] == st[i + 1]:
		if len(mp) == 0:
			mp = st[i - 1:i + 2]
		elif len(mp) == 3:
			if st[i - 1:i + 2] < mp:
				mp = st[i - 1:i + 2]
if st[-1] == st[-2]:
	if len(mp) == 0 or len(st[-2:]) < len(mp):
		mp = st[-2:]
	elif st[-2:] < mp:
		mp = st[-2:]
print(-1 if len(mp) == 0 else mp)
