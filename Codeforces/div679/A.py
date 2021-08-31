def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


for t_ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    for i in range(n // 2):
        lcmn = lcm(s[i * 2], s[i * 2 + 1])
        print(lcmn // s[i * 2], -(lcmn // s[i * 2 + 1]), end=' ')
    print()
