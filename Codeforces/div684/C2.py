
def generate(x1, x2, n1, n2):
    ans = []
    if x1 != n1 or x2 != n2:
        ans.append(x1)
        ans.append(x2)
    if x1 + 1 != n1 or x2 != n2:
        ans.append(x1 + 1)
        ans.append(x2)
    if x1 != n1 or x2 + 1 != n2:
        ans.append(x1)
        ans.append(x2 + 1)
    if x1 + 1 != n1 or x2 + 1 != n2:
        ans.append(x1 + 1)
        ans.append(x2 + 1)
    return ans


def set(r, c, i, arr):
    if i == 1:
        arr[r][c + 1] = 0
        arr[r + 1][c] = 0
        arr[r + 1][c + 1] = 0
    elif i == 2:
        arr[r + 1][c] = 0
        arr[r][c] = 0
        arr[r + 1][c + 1] = 0
    elif i == 3:
        arr[r][c + 1] = 0
        arr[r][c] = 0
        arr[r + 1][c + 1] = 0
    else:
        arr[r][c + 1] = 0
        arr[r + 1][c] = 0
        arr[r][c] = 0

def gen_seq(x1, x2, c):
    ans = []
    x1 += 1
    x2 += 1
    for i in c:
        if i == 1:
            ans.append(generate(x1, x2, x1, x2))
        elif i == 2:
            ans.append(generate(x1, x2, x1, x2 + 1))
        elif i == 3:
            ans.append(generate(x1, x2, x1 + 1, x2))
        else:
            ans.append(generate(x1, x2, x1 + 1, x2 + 1))
    return ans


for t in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(map(int, list(input()))) for i in range(n)]
    ans = []
    count = 0
    for r in range(n - 1):
        for c in range(n - 1):
            if arr[r][c] + arr[r + 1][ c] + arr[r][ c + 1] + arr[r + 1][ c + 1] >= 3:
                if arr[r][ c] == 0:
                    ans.append(generate(r, c, r, c))
                    set(r, c, 1, arr)
                elif arr[r + 1][c] == 0:
                    ans.append(generate(r, c, r + 1, c))
                    set(r, c, 3, arr)
                elif arr[r][ c + 1] == 0:
                    ans.append(generate(r, c, r, c + 1))
                    set(r, c, 2, arr)
                else:
                    ans.append(generate(r, c, r + 1, c + 1))
                    set(r, c, 4, arr)
                count += 1
    for row in range(n):
        for col in range(m):
            r = row
            c = col
            if arr[row][col] == 0:
                continue
            if c == 0 and r == 0:
                for i in gen_seq(r, c, (3, 2, 4)):
                    ans.append(i)
            elif row == 0:
                for i in gen_seq(r, c - 1, (4, 1, 3)):
                    ans.append(i)
            elif col == 0:
                for i in gen_seq(r - 1, c, (4, 1, 2)):
                    ans.append(i)
            else:
                for i in gen_seq(r - 1, c - 1, (3, 2, 1)):
                    ans.append(i)
            count += 3

    print(count)
    # print('\n'.join([' '.join(map(str, i)) for i in arr]))
    for i in ans:
        print(' '.join(map(str, i)))
