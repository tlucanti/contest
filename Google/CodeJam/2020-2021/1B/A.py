
import itertools
p = 1000000000
pp = 360 * 12 * pow(10, 10)

for t in range(int(input())):
	a_, b_, c_ = map(int, input().split())
	f = 0
	for i in range(60 * 60 * 12):
		if f:
			break
		for (h_, m_, s_) in itertools.permutations((a_, b_, c_)):
			n1 = h_ % 1000000000
			s1 = (h_ // 1000000000) % 60
			m1 = (h_ // 1000000000 // 60) % 60
			h1 = (h_ // 1000000000 // 60 // 60) % 12

			n2 = (m_ // 12) % 1000000000
			s2 = (m_ // 12 // 1000000000) % 60
			m2 = (m_ // 12 // 1000000000 // 60) % 60

			n3 = (s_ // 720) % 1000000000
			s3 = (s_ // 720 // 1000000000) % 60

			if n1 == n2 == n3 and s1 == s2 == s3 and m1 == m2:
				# print(h_, m_, s_)
				print(f'Case #{t + 1}: {h1} {m1} {s1} {n1}')
				# print(0, m2, s2, n2)
				# print(0, 0, s3, n3)
				# print()
				f = 1
				break

		a_ += p
		b_ += p
		c_ += p
		a_ %= pp
		b_ %= pp
		c_ %= pp
