
a = input().split()
s = 0
si = 0
for i in a:
    d = a.count(i)
    if d > s:
        s = d
        si = i
print(si)
