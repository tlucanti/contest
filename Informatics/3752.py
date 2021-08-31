
l = input().split()
s = set()
for i in l:
    n = len(s)
    s.add(i)
    print("YES" if n == len(s) else "NO")