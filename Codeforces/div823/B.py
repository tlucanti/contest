
def inp():
    return list(map(int, input().split()))

def list_rindex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1

for _ in range(int(input())):
    n = int(input())
    x = inp()
    t = inp()

    #for i in range(n):
    #    x[i] += t[i]

    tm = max(t)
    tl = t.index(tm)
    tr = list_rindex(t, tm)
    mid = (x[tl] + x[tr]) / 2
    #print('mid', mid, tm, tl, tr)

    for i in range(n):
        if abs(x[i] - mid) + t[i]  <= tm:
            x[i] = mid
        else:
            if x[i] > mid:
                x[i] -= tm - t[i] 
            else:
                x[i] += tm - t[i]

    print((max(x) + min(x)) / 2)
