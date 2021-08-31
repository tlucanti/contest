
def factor2(n):
    i = 0
    while n % 2 == 0:
        i += 1
        n //= 2
    return i


for t in range(int(input())):
    h, w, n = map(int, input().split())
    if pow(2, factor2(h)) * pow(2, factor2(w)) >= n:
        print("YES")
    else:
        print('NO')
