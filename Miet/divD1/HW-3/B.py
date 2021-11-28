
def divisors(n):
	ans = []
	for i in range(1, n + 1):
		if n % i == 0:
			ans.append(i)
	return ans


def check_div(s, n):
	div = a[:n]
	for i in range(len(s) // n):
		if s[n * i:n * (i + 1)] != div:
			return False
	return True


a, b = input(), input()
divs = divisors(len(a))
ans = 0
for div in divs:
	if len(b) % div != 0:
		continue
	if not check_div(a, div):
		continue
	if not check_div(b, div):
		continue
	if a[:div] != b[:div]:
		continue
	ans += 1
print(ans)
