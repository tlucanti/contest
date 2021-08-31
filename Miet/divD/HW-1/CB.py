
n = int(input())
c = input().split('1')
s = 1
l = len(c)
if l == 1:
    print(0)
else:
    for i in range(1, l - 1):
        s *= c[i].count('0') + 1
    print(s)
