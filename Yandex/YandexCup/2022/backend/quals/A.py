
def inp():
    return list(map(int, input().split()))

n, m, q = inp()
data = [set() for _ in range(n)]
resets = [0] * n

max_ra = 0
max_num = 0
min_ra = 0
min_num = 0

for _ in range(q):
    a = input()
    if a == 'GETMAX':
        print(max_num + 1)
        continue
    elif a == 'GETMIN':
        print(min_num + 1)
        continue
    elif a.startswith('RESET'):
        _, num = a.split()
        num = int(num) - 1
        resets[num] += 1
        data[num] = set()
        new_val = resets[num] * m
    else:
        _, dc, s = a.split()
        dc = int(dc) - 1
        s = int(s) - 1
        data[dc].add(s)
        new_val = resets[dc] * (m - len(data[dc]))
        num = dc

    if (new_val == max_ra):
        max_num = min(max_num, num)
    elif (new_val > max_ra):
        max_ra = new_val
        max_num = num
    if (new_val == min_ra):
        min_num = min(min_num, num)
    elif (new_val < min_ra):
        min_ra = new_val
        min_num = num

