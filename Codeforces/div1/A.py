for t in range(int(input())):
	n = int(input())
	s = input().split()
	st = list(set(s));
	if s.count(st[0]) == 1:
		print(s.index(st[0]) + 1)
	else:
		print(s.index(st[1]) + 1)
	