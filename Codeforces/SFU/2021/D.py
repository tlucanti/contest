
def pr():
	for i in a_even:
		print(' '.join(map(str, i)))
	print()
	for i in a_odd:
		print(' '.join(map(str, i)))
	print()
	print()


n, k = map(int, input().split())
s = list(map(int, input().split()))
even = 0
odd = 0
for i in s:
	if i % 2:
		odd += 1
	else:
		even += 1

# четный
# нечетный
a_even = [[1 for i in range(even + 1)] for j in range(odd + 1)]
a_odd = [[1 for i in range(even + 1)] for j in range(odd + 1)]

a_odd[0][0] = -1
a_even[0][0] = -1
for i in range(1, even + 1):
	a_even[0][i] = 0
for i in range(1, odd + 1):
	a_odd[i][0] = 0

pr()
for t in range(2, n - k + 2):
	a_even_new = [[1 for i in range(even + 1)] for j in range(odd + 1)]
	a_odd_new = [[1 for i in range(even + 1)] for j in range(odd + 1)]

	for row in range(odd + 1):
		for col in range(even + 1):
			if row + col < t:
				a_even_new[row][col] = -1
				a_odd_new[row][col] = -1
				continue
			if row == 0:
				a_even_new[0][col] = a_even[0][col - 1]
				a_odd_new[0][col] = a_odd[0][col - 1]
			elif col == 0:
				a_even_new[row][0] = a_odd[row - 1][0]
				a_odd_new[row][0] = a_even[row - 1][0]
			else:
				a_even_new[row][col] = int ((a_even[row][col - 1] + a_odd[row - 1][col]) > 0)
				a_odd_new[row][col] = int ((a_odd[row][col - 1] + a_even[row - 1][col]) > 0)
	a_even = a_even_new
	a_odd = a_odd_new
	pr()

print('S' if a_even[odd][even] else 'D')
