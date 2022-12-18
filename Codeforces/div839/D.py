
def inp():
    return list(map(int, input().split()))

def find(a):
    for i in range(max(a) + 1):
        b = [abs(i - j) for j in a]
        if b == sorted(b):
            print(i)

def conv(a):
    b = [0] * (len(a) - 1)
    for i in range(1, len(a)):
        b[i - 1] = a[i] - a[i - 1]
    return b

def upd(a, b):
    return (a + b) // 2 + (a + b) % 2

for _ in range(int(input())):
    n = int(input())
    a = inp()
    n = len(a)
    if n == 1:
        print(0)
        continue
    rng = [0, a[0]]
    for i in range(1, n):
        if a[i] == a[i - 1]:
            continue
        if a[i] > a[i - 1]:
            rng[1] = min(rng[1], upd(a[i], a[i - 1]))
        else:
            rng[0] = max(rng[0], upd(a[i], a[i - 1]))
    if 0: # rng[0] > rng[1]:
        print(-1)
        continue
    else:
        ok = False
        ans = 0
        for i in range(rng[0], rng[0] + 1):
            b = [abs(i - j) for j in a]
            if b == sorted(b):
                ans = i
                ok = True
                break
        if ok:
            print(ans)
        else:
            print(-1)


