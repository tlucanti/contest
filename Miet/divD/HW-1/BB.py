def print_state(_n, _b1, _b2):
    print('a' * (n - _b1 - 1), end='')
    print('b', end='')
    print('a' * (_b1 - _b2), end='')
    print('b', end='')
    print('a' * (_b2 - 1))


t = int(input())
for _t in range(t):
    n, k = input().split()
    n, k = int(n), int(k)
    b1 = 0
    b2 = 0
    s = 0
    for i in range(n):
        s += i
        if s >= k:
            b1 = i
            s -= i
            break
    b2 = k - s
    print_state(n, b1, b2)
