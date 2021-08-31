
t = int(input())
for i in range(t):
    a, b, c, d = map(int, input().split())
    ans = ['Tidak', 'Tidak', 'Tidak', 'Tidak']
    if ((a + b) % 2 == 1) and ((a + d) > 0):
        ans[0] = 'Ya'
    if ((a + b) % 2 == 1) and (((a + d) == 0) or ((b + c) > 0)):
        ans[1] = 'Ya'
    if ((a + b) % 2 == 0) and (((a + d) == 0) or ((b + c) > 0)):
        ans[2] = 'Ya'
    if ((a + b) % 2 == 0) and ((a + d) > 0):
        ans[3] = 'Ya'
    print(' '.join(ans))
