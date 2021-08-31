def mss(matr, arr):
    ans = 0
    for i in range(len(matr)):
        for j in range(len(matr)):
            if matr[i][j]:
                if arr[i] != arr[j]:
                    ans += 1
    return ans // 2


n = int(input())
matr = [list(map(int, input().split())) for _ in range(n)]
_ = input()
arr = list(map(int, input().split()))
print(mss(matr, arr))
