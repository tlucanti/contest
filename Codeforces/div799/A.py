for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(sum([b > a, c > a, d > a]))
