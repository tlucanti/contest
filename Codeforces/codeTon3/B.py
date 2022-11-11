
def inp():
    return list(map(int, input().split()))

def convolve(a):
    ans = []
    if len(a) == 0:
        return ans
    c = a[0]
    n = 0
    for i in a:
        if i == c:
            n += 1
        else:
            ans.append((c, n))
            c = i
            n = 1
    ans.append((c, n))
    return ans

for _ in range(int(input())):
    n = int(input())
    a = input()
    ans = 0
    cnv = convolve(a)
    for i in cnv:
        ans = max(ans, i[1] * i[1])
    print(max(ans, a.count('0') * a.count('1')))

