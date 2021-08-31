
a = map(int, input().split())
m = 0
for i in a:
    if i % 2:
        m = i if m == 0 else min(m, i)
print(m)
