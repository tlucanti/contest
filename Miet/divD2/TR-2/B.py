
from collections import Counter as multiset

def inp():
    return list(map(int, input().split()))

n = int(input())
a = inp()
d = multiset(a)
aa = [0] * len(d)
ii = 0
for i in d:
    aa[ii] = [i, i * d[i], i * d[i]]
    if i + 1 in d:
        aa[ii][1] -= (i + 1) * d[i + 1]
    if i - 1 in d:
        aa[ii][1] -= (i - 1) * d[i - 1]
    ii += 1

aa.sort(key=lambda x: x[1], reverse=True)
took = set()
ans = 0
print(aa)
for i in range(len(aa)):
    if aa[i][0] not in took:
        ans += aa[i][2]
        took.add(aa[i][0])
        took.add(aa[i][0] + 1)
        took.add(aa[i][0] - 1)
print(ans)


