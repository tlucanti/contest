
def inp():
    return list(map(int, input().split()))

def __s(A, B):
    if i >= len(A) and i >= len(B):
        pass
    if i < len(A) and i < len(B):
        a1 += A[i] * 2 + B[i] * 2
    elif i < len(A):
        a1 += A[i]
    elif i < len(B):
       a1 += B[i]

    if len(A) > 0:
        a1 -= A[-1]
    
    return a1

def solve(A, B):
    aa = False
    bb = False
    ans = 0

    if len(A) > 0:
        ans = A[-1]
        aa = True
    for i in range(max(len(A), len(B)) + 1):
        if i < len(B):
            if aa:
                ans += B[i] * 2
            else:
                ans += B[i]
            bb = True
        else:
            bb = False

        if i < len(A) - 1:
            if bb:
                ans += A[i] * 2
            else:
                ans += A[i]
            aa = True
        else:
            aa = False

    return ans

for _ in range(int(input())):
    n = int(input())
    a = inp()
    b = inp()

    A = [b[i] for i in range(n) if a[i] == 0]
    B = [b[i] for i in range(n) if a[i] == 1]

    A.sort(reverse=True)
    B.sort(reverse=True)

    print(max(solve(A, B), solve(B, A)))

