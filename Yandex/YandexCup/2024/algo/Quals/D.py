
def solve():
    low = 1
    high = 2

    while True:
        print(high, flush=True)
        res = input()
        if res == 'wet':
            low = high
            high *= 2
        elif res == 'ok':
            break
        else:
            assert False

    if high == 2:
        print(1, flush=True)
        res = input()
        if res == 'ok':
            return 1
        elif res == 'wet':
            return 2
        else:
            assert False

    while high - low > 1:
        mid = (low + high) // 2
        print(mid, flush=True)
        res = input()

        if res == 'wet':
            low = mid
        elif res == 'ok':
            high = mid
        else:
            assert False

    return high

print('!', solve(), flush=True)





