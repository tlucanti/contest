
def sgn(z):
    if z > 0:
        return 1
    elif z < 0:
        return -1
    else:
        return 0


def v_mul(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


def check(x, y):
    v = (x, y)
    s = {sgn(v_mul(v1, (x - d, y))), sgn(v_mul(v2, (x, y - d))),
         sgn(v_mul(v3, (x - n + d, y - n))), sgn(v_mul(v4, (x - n, y - n + d)))}
    if -1 in s and 1 in s:
        return False
    else:
        return True


n, d = map(int, input().split())
k = int(input())
v1 = (-d, d)
v2 = (n - d, n - d)
v3 = (d, -d)
v4 = (-n + d, -n + d)
for i in range(k):
    x, y = map(int, input().split())
    if check(x, y):
        print('YES')
    else:
        print('NO')
