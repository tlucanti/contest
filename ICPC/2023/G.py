
k = int(input())
X = int(input())

x = f'{X:064b}'[::-1]

s = x[63][::-1]
m = x[:k][::-1]
e = x[k:63][::-1]

s = int(s, 2)
m = int(m, 2)
e = int(e, 2)

ans = None

if e == 2 ** (63 - k) - 1:
    ans = 'NaN'
    print(ans)
else:
    if e > 0:
        e = e + 1 - 2**(62 - k)
    elif e == 0:
        e = 1 - 2 ** (62 - k)
    else:
        assert False

    ans = 2**e + m * 2 ** (e - k)
    ans = int(ans)
    a2 = 0
    while ans % 2 == 0:
        ans //= 2
        a2 += 1
    if s != 0:
        print(end='-')
    if a2 != 0:
        print(f'{ans}*2**{a2}')
    else:
        print(ans)

