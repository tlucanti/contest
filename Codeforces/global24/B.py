
def inp():
    return list(map(int, input().split()))

def factor(n):
    ans = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            n //= i
        else:
            i += 1
    if n != 0:
        ans.append(n)
    return ans

def prod(a):
    ans = 1
    for i in a:
        ans *= i
    return ans

for _ in range(int(input())):
    n = int(input())
    a = list(set(inp()))
    n = len(a)
    divs = factor(a[0])
    for i in range(1, n):
        if len(divs) == 0:
            break
        dd = []
        aa = a[i]
        for d in divs:
            if aa % d == 0:
                dd.append(d)
                aa //= d
        divs = dd

    if len(divs) == 0:
        print(max(a))
    else:
        print(max(a) // prod(divs))

