
from string import ascii_lowercase as alp
from string import digits

def inp():
    return list(map(int, input().split()))


def convert(nn, aa):
    ans = 0
    for i in nn:
        ans = ans * aa + i
    return ans

def count(nn, aa):
    ans = 0
    for i in nn:
        ans = ans * 10 + a[i]
    return ans

for _ in range(int(input())):
    n, b = inp()
    a = []
    for i in range(10):
        if i % b == 0:
            a.append(i)
    num = [0] * 18
    pos = 0
    while True:
        if pos >= 18:
            break
        num[pos] += 1
        if num[pos] == len(a):
            num[pos] -= 1
            pos += 1
            continue
        cc = count(num, a)
        if cc == n:
            break
        elif cc > n:
            num[pos] -= 1
            pos += 1
    print(convert(num, len(a)))

