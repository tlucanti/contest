
import sys


def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    s = set(range(1, n + 1))
    prev = 0
    left, right = 1, n
    direct = 0
    while True:
        if len(s) == 1:
            break
        if len(s) == prev:
            if direct:
                left, right = right, right + (right - left)
            else:
                left, right = left - (right - left), left
            direct = 1 - direct
        d = (right - left) // 2
        if direct == 0:
            right -= d
        else:
            left += d
        print(f'? {left} {right}')
        sys.stdout.flush()
        a = set(inp())
        prev = len(s)
        for i in a:
            if i not in range(left, right + 1):
                s.discard(i)
        for i in range(left, right + 1):
            if i not in a:
                s.discard(i)
        # print(s)
        # direct = 1 - direct

    # print(s)
    print(f'! {s.pop()}')
    sys.stdout.flush()
