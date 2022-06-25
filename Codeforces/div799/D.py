 
def check_pal(x):
    h = x // 60
    m = x % 60
    t = f'{h:02}:{m:02}'
    return t == t[::-1]
 
 
for _ in range(int(input())):
    t, x = input().split()
    t = t.split(':')
    t = int(t[0]) * 60 + int(t[1])
    x = int(x)
    t0 = t
    ans = 0
    while True:
        ans += check_pal(t)
        t = (t + x) % (24 * 60)
        if t == t0:
            break
    print(ans)
