
for t in range(int(input())):
    n, c0, c1, h = map(int, input().split())
    s = input()
    _0 = s.count('0')
    _1 = s.count('1')
    print(min(c0 * _0 + c1 * _1, c0 * len(s) + h * _1, c1 * len(s) + h * _0))
