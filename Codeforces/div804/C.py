
import itertools


def inp():
    return list(map(int, input().split()))


def mex(a):
    aa = set(a)
    for i in range(len(a) + 1):
        if i not in aa:
            return i


def check_mex(a, p):
    for i in range(len(a) + 1):
        for j in range(i + 1, len(a) + 1):
            if mex(a[i:j]) != mex(p[i:j]):
                return False
    return True


def solve(a):
    a = tuple(a)
    n = len(a)
    ans = 0
    for p in itertools.permutations(a):
        if p == a:
            continue
        if check_mex(a, p):
            # print(p)
            ans += 1
    return ans + 1


# print(solve([1, 2, 4, 0, 5, 3]))
# print(solve([6,5,0,4,2,3,1]))
# print(solve([7,1,5,2,3,0,4,6]))
for i in range(6):
    a = set()
    for pr in itertools.permutations(list(range(1, i))):
        A = [i, 0] + list(pr)
        sl = solve(A)
        # print(A, sl)
        a.add(sl)
    print(a)
