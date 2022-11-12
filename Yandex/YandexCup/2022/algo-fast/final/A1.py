
def inp():
    return list(map(int, input().split()))

n = input()
a = inp()
b = inp()
n = len(a)

a.sort(reverse=True)
b.sort(reverse=True)
ai = 0
bi = 0
ans = 0
end = []
while ai < n and bi < n:
    if a[ai] > b[bi]:
        ans += 1
        ai += 1
        bi += 1
    else:
        end.append(b[bi])
        bi += 1
bi = 0
end = end[::-1]
while bi < len(end) and ai < n:
    if end[bi] > a[ai]:
        ans -= 1
    ai += 1
    bi += 1

ai = 0
bi = 0
ans2 = 0
end = []
while ai < n and bi < n:
    if a[ai] > b[bi]:
        ans2 += 1
        ai += 1
        bi += 1
    elif a[ai] == b[bi]:
        ai += 1
        bi += 1
    else:
        end.append(b[bi])
        bi += 1

bi = 0
end = end[::-1]
while bi < len(end) and ai < n:
    if end[bi] > a[ai]:
        ans2 -= 1
    ai += 1
    bi += 1

ans3 = ans
ans4 = ans2

a.sort()
b.sort()
ai = 0
bi = 0
ans = 0
end = []
while ai < n and bi < n:
    if a[ai] > b[bi]:
        ans += 1
        ai += 1
        bi += 1
    else:
        end.append(a[ai])
        ai += 1
ai = 0
end = end[::-1]
while ai < len(end) and bi < n:
    if end[ai] < b[bi]:
        ans -= 1
    ai += 1
    bi += 1

ai = 0
bi = 0
ans2 = 0
end = []
while ai < n and bi < n:
    if a[ai] > b[bi]:
        ans2 += 1
        ai += 1
        bi += 1
    elif a[ai] == b[bi]:
        ai += 1
        bi += 1
    else:
        end.append(a[ai])
        ai += 1

ai = 0
end = end[::-1]
while ai < len(end) and bi < n:
    if end[ai] < b[bi]:
        ans2 -= 1
    ai += 1
    bi += 1


print(max(ans, ans2, ans3, ans4))

