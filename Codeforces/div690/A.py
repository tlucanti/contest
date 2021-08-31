
for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    i = n // 2
    ar = []
    if n % 2:
        sig = -1
    else:
        sig = 1
    for j in range(n):
        i = i + j * sig
        ar.append(s[i])
        sig *= -1
    print(*(ar[::-1]))
