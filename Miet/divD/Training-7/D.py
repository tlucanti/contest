
n = int(input())
s = list(map(int, input().split()))
ans = 0
# 1 - circle
# 2 - triangle
# 3 - square
for i in range(1, n):
    if s[i - 1] == 1:
        if s[i] == 2:
            if i - 2 >=0 and s[i - 2] == 3:
                ans += 2
            else:
                ans += 3
        elif s[i] == 3:
            ans += 4
    elif s[i - 1] == 3:
        if s[i] == 1:
            ans += 4
        elif s[i] == 2:
            ans = 'Infinite'
            break
    else: # 2
        if s[i] == 1:
            ans += 3
        elif s[i] == 3:
            ans = 'Infinite'
            break
if ans == 'Infinite':
    print(ans)
else:
    print('Finite')
    print(ans)
