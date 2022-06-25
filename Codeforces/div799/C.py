for _ in range(int(input())):
    input()
    m = [input() for i in range(8)]
    for i in range(1, 7):
        for j in range(1, 7):
            if m[i][j] == m[i + 1][j + 1] == m[i - 1][j - 1] == m[i + 1][j - 1] == m[i - 1][j + 1] == '#':
                print(i + 1, j + 1)
                break
