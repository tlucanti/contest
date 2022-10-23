
def inp():
    return list(map(int, input().split()))

n = int(input())
a = inp()
s = dict()
for i in a:
    s[i] = s.get(i, 0) + 1
    print(s[i], end=' ')
print()

