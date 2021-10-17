st = input()
mp = ''
c = 0
p = ''
for i in range(1, len(st) - 1):
	if st[i - 1] == st[i]:
		p = st[i - 1:i + 1]
	elif st[i - 1] == st[i + 1]:
		p = st[i - 1:i + 2]
	else:
		continue
	if len(mp) == 0 or len(p) < len(mp):
		mp = p
	elif p < mp:
		mp = p
if st[-1] == st[-2]:
	if len(mp) == 0 or len(st[-2:]) < len(mp):
		mp = st[-2:]
	elif st[-2:] < mp:
		mp = st[-2:]
print(-1 if len(mp) == 0 else mp)
