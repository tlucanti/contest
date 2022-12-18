
n = int(input())
last = 0
last_beg = 0
for i in range(1, n + 1):
    if i * 100 // n != last:
        print(last, last_beg, i - 1)
        last += 1
        last_beg = i

