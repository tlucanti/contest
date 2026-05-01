
def mex(v):
    v.sort()
    for i in range(len(v)):
        if i != v[i]:
            #print('mex', v, i)
            return i
    #print('mex', v, len(v))
    return len(v)

for _ in range(int(input())):
    n = int(input()) * 2
    s = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        v = []
        for d in range(n):
            if i - d < 0 or i + d >= n:
                break
            if s[i - d] == s[i + d]:
                v.append(s[i - d])
            else:
                break
        #print(i, v)
        ans = max(ans, mex(v))

    for i in range(n):
        v = []
        for d in range(n):
            if i - d < 0 or i + d + 1 >= n:
                break
            if s[i - d] == s[i + d + 1]:
                v.append(s[i - d])
            else:
                break
        #print(i, v)
        ans = max(ans, mex(v))

    print(ans)
