
def inp():
    return [int(_) for _ in input().split()]

def get_next(idx, ar):
    v = ar[idx]
    return next_v(idx, v, ar)

def next_v(idx, v, ar):
    for i in range(idx + 1, len(ar)):
        if ar[i] == v:
            return i
    return None

def prev_v(idx, v, ar):
    for i in range(idx - 1, -1, -1):
        if ar[i] == v:
            return i
    return None

def solve():
    t, n = inp()
    a = inp()

    if n == t:
        print(n)
        return
    elif n == 1:
        print(1)
        return

    b = sorted(a)
    safe = None
    left = n

    for i in range(len(a)):
        left -= 1
        if b[i] != b[i + 1]:
            safe = b[i]
        if left == 0:
            break

    if safe is None:
        mn = min(a)
        l = a.index(mn)
        r = l
        for i in range(n - 1):
            r = get_next(r, a)
            assert r is not None
        #print('#2', l, r)
        ans = r - l + 1

        while True:
            r = get_next(r, a)
            #print('#3', l, r)
            if r is None:
                break
            l = get_next(l, a)
            #print('#4', l, r)
            ans = min(ans, r - l + 1)

        print(ans)
        return

    else:
        island_left = None
        island_right = None
        volatile = b[n]

        for i in range(len(a)):
            if a[i] <= safe:
                island_left = i
                break

        for i in range(len(a) - 1, -1, -1):
            if a[i] <= safe:
                island_right = i
                break

        left = n
        for i in range(island_left, island_right + 1):
            if a[i] <= safe:
                left -= 1
        assert left >= 0

        for i in range(island_left, island_right + 1):
            if left == 0:
                break
            if a[i] == volatile:
                left -= 1

        # print('#1', island_left, island_right, left, volatile)
        if left == 0:
            print(island_right - island_left + 1)
            return

        l = island_left - 1
        r = island_right + 1
        la = island_left
        ra = island_right

        while True:
            if l >= 0 and a[l] == volatile:
                left -= 1
                la = l
                if left == 0:
                    break
            if r < len(a) and a[r] == volatile:
                left -= 1
                ra = r
                if left == 0:
                    break

            l -= 1
            r += 1
            assert l >= 0 or r < len(a)

        assert left == 0
        print(ra - la + 1)
        return

solve()

