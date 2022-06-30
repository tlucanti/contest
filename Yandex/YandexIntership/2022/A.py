
def inp():
    return list(map(int, input().split()))


n = int(input())
a = inp()

w = 0
ht = {1 << x : chr(ord('a') + x) for x in range(26)}
ht[1 << 26] = ' '

for i in range(n):
    b = w ^ a[i]
    print(ht[b], end='')
    w = a[i]
print()
