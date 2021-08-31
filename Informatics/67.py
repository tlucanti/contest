
n = input()
a = list(map(int, input().split()))
s = 0
for i in range(len(a) - 1):
    s += a[i + 1] * a[i] > 0
    if s:
        break

print("YES" if s else "NO")
