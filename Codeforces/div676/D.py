
for t in range(int(input())):
    x, y = input().split()
    x, y = int(x), int(y)
    c1, c2, c3, c4, c5, c6 = map(int, input().split())

    if x > 0 and y > 0:
        print(max(
            c6 * y + c6 * x,

        ))